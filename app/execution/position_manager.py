class PositionManager:
    def __init__(self):
        self.positions = {}

    def open_position(self, user_id, symbol, side, entry, size, leverage=1):
        self.positions[(user_id, symbol)] = {
            "side": side,
            "entry": entry,
            "size": size,
            "leverage": leverage,
            "sl": None,
            "tp": None,
            "trailing": None
        }

    def update_protection(self, user_id, symbol, sl=None, tp=None, trailing=None):
        pos = self.positions.get((user_id, symbol))
        if not pos:
            return
        if sl:
            pos["sl"] = sl
        if tp:
            pos["tp"] = tp
        if trailing:
            pos["trailing"] = trailing

    def close_position(self, user_id, symbol):
        self.positions.pop((user_id, symbol), None)

    def get(self, user_id, symbol):
        return self.positions.get((user_id, symbol))

    def has_position(self, user_id, symbol):
        return (user_id, symbol) in self.positions
