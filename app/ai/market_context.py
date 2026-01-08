class MarketContext:
    def __init__(self, symbol, timeframe, market_state, structure, indicators):
        self.symbol = symbol
        self.timeframe = timeframe
        self.market_state = market_state
        self.structure = structure
        self.indicators = indicators

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "market_state": self.market_state,
            "structure": self.structure,
            "indicators": self.indicators
        }
