import ta

def indicators(df):
    return {
        "rsi": ta.momentum.rsi(df["close"], 14).iloc[-1],
        "ema_fast": ta.trend.ema_indicator(df["close"], 20).iloc[-1],
        "ema_slow": ta.trend.ema_indicator(df["close"], 50).iloc[-1],
        "macd": ta.trend.macd_diff(df["close"]).iloc[-1]
    }
