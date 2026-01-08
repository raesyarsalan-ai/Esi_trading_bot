class PositionManager:
    def __init__(self):
        self.positions = {}

    def has_position(self, user_id, symbol):
        return self.positions.get((user_id, symbol)) is not None

    def open_position(self, user_id, symbol, price, side):
        self.positions[(user_id, symbol)] = {
            "entry": price,
            "side": side
        }

    def close_position(self, user_id, symbol):
        self.positions.pop((user_id, symbol), None)
