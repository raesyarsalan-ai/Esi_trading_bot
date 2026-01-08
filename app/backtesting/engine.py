class BacktestEngine:
    def __init__(self, lifecycle, data):
        self.lifecycle = lifecycle
        self.data = data
        self.balance = 1000

    def run(self):
        for i in range(100, len(self.data)):
            df = self.data.iloc[:i]
            price = df.iloc[-1].close
            self.lifecycle.step(df, "BTC/USDT", "5m")
        return self.balance
