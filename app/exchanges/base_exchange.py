class BaseExchange:
    def __init__(self, ccxt_client):
        self.client = ccxt_client

    def fetch_ohlcv(self, symbol, timeframe, limit=200):
        return self.client.fetch_ohlcv(symbol, timeframe, limit=limit)

    def create_order(self, symbol, side, amount, price=None, params=None):
        raise NotImplementedError
