from app.execution.order_validator import OrderValidator

class OrderExecutor:
    def __init__(self, exchange):
        self.exchange = exchange
        self.validator = OrderValidator()

    def execute(self, symbol, side, amount):
        self.validator.validate(symbol, side, amount)
        return self.exchange.create_order(symbol, side, amount)
