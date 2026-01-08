class BotEngine:
    def __init__(self, user, exchange, executor):
        self.user = user
        self.exchange = exchange
        self.executor = executor

    def trade(self, decision, symbol, amount):
        if not self.user.can_trade():
            raise PermissionError("User not allowed to trade")
        return self.executor.execute(symbol, decision, amount)
