class OrderExecutor:
    def __init__(self, exchange):
        self.exchange = exchange

    def market(self, symbol, side, amount, params=None):
        return self.exchange.create_order(
            symbol=symbol,
            side=side,
            amount=amount,
            params=params or {}
        )

    def close(self, symbol, side, amount):
        close_side = "sell" if side == "buy" else "buy"
        return self.market(symbol, close_side, amount)
