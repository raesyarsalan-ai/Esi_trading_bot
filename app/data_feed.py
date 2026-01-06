import pandas as pd

def fetch_ohlcv(exchange, symbol, timeframe, limit=100):
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

    df = pd.DataFrame(
        data,
        columns=["time", "open", "high", "low", "close", "volume"]
    )

    df["time"] = pd.to_datetime(df["time"], unit="ms")
    return df
