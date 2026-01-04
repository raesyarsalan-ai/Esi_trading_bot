import pandas as pd

def fetch_ohlcv(exchange, symbol, timeframe, limit=100):
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    return pd.DataFrame(
        data,
        columns=["time", "open", "high", "low", "close", "volume"]
    )
