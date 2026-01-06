from app.analysis.market_state import detect_market_state
from app.analysis.range_detection import is_range
from app.decision_engine import decide
from backtesting.metrics import max_drawdown, win_rate

class BacktestRunner:
    def __init__(self, data, initial_balance=1000):
        self.data = data
        self.balance = initial_balance
        self.equity_curve = [initial_balance]
        self.position = None
        self.trades = []

    def run(self):
        for i in range(50, len(self.data)):
            df = self.data.iloc[:i]
            price = df.iloc[-1].close

            market = detect_market_state(df)
            range_market = is_range(df)

            signals = {
                "trend": 1 if market == "bull" else -1,
                "range": -1 if range_market else 1
            }

            decision = decide(signals)

            if decision == "buy" and not self.position:
                self.position = price

            elif decision == "sell" and self.position:
                pnl = price - self.position
                self.balance += pnl
                self.trades.append(pnl)
                self.position = None

            self.equity_curve.append(self.balance)

        return {
            "final_balance": self.balance,
            "max_drawdown": max_drawdown(self.equity_curve),
            "win_rate": win_rate([(p,) for p in self.trades]),
            "trades": len(self.trades)
        }
