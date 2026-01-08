from app.ai.market_context import MarketContext
from app.analysis.technical.indicators import indicators
from app.analysis.technical.market_structure import market_structure
from app.analysis.technical.trend import trend
from app.strategies.strategy_selector import StrategySelector

class Lifecycle:
    def __init__(self, ai_engine, risk_engine):
        self.selector = StrategySelector()
        self.ai = ai_engine
        self.risk = risk_engine

    def step(self, df, symbol, timeframe):
        inds = indicators(df)
        structure = market_structure(df)
        mkt = trend(inds)

        context = MarketContext(
            symbol, timeframe, mkt, structure, inds
        )

        ai_result = self.ai.analyze(context)
        if not ai_result:
            return None

        decision = self.selector.select(context, ai_result)
        if not decision:
            return None

        risk = self.risk.approve(ai_result["confidence"])
        return decision, risk
