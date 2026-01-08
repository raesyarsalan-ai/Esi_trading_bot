from app.strategies.base_strategy import BaseStrategy

class RangeTrading(BaseStrategy):
    def decide(self, context, ai_bias):
        if context.structure == "range" and ai_bias == "neutral":
            return "buy"
        return None
