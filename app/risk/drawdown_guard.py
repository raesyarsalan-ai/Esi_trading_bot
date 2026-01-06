class DrawdownGuard:
    def __init__(self, max_dd):
        self.max_dd = max_dd
        self.peak = None

    def allow(self, equity):
        # اگر هنوز موجودی واقعی نداریم، ترید را متوقف نکن
        if equity is None or equity <= 0:
            return True

        # اولین بار، peak را مقداردهی کن
        if self.peak is None:
            self.peak = equity
            return True

        if equity > self.peak:
            self.peak = equity
            return True

        dd = (self.peak - equity) / self.peak
        return dd < self.max_dd
