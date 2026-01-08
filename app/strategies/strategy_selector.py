from app.strategies.trend_following import TrendFollowing
from app.strategies.range_trading import RangeTrading

class StrategySelector:
    def __init__(self):
        self.strategies = [
            TrendFollowing(),
            RangeTrading()
        ]

    def select(self, context, ai_result):
        for strat in self.strategies:
            decision = strat.decide(context, ai_result["bias"])
            if decision:
                return decision
        return None
