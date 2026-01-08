class BrokerSimulator:
    def __init__(self, balance):
        self.balance = balance
        self.position = None

    def open(self, price):
        self.position = price

    def close(self, price):
        pnl = price - self.position
        self.balance += pnl
        self.position = None
        return pnl
