class StateManager:
    def __init__(self):
        self.state = {}

    def in_position(self, user, symbol):
        return self.state.get((user.user_id, symbol)) is not None

    def set_position(self, user, symbol, data):
        self.state[(user.user_id, symbol)] = data

    def clear(self, user, symbol):
        self.state.pop((user.user_id, symbol), None)
