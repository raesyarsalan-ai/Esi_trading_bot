from app.strategies.base_strategy import BaseStrategy

class TrendFollowing(BaseStrategy):
    def decide(self, context, ai_bias):
        if context.market_state == ai_bias == "bull":
            return "buy"
        if context.market_state == ai_bias == "bear":
            return "sell"
        return None
