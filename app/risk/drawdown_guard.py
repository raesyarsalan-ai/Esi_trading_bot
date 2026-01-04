class DrawdownGuard:
    def __init__(self, max_dd):
        self.max_dd = max_dd
        self.peak = None

    def allow(self, equity):
        if self.peak is None or equity > self.peak:
            self.peak = equity
        dd = (self.peak - equity) / self.peak
        return dd < self.max_dd
