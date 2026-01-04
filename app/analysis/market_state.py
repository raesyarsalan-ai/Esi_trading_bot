import ta

def detect_market_state(df):
    ema_fast = ta.trend.ema_indicator(df["close"], 20)
    ema_slow = ta.trend.ema_indicator(df["close"], 50)

    if ema_fast.iloc[-1] > ema_slow.iloc[-1]:
        return "bull"
    if ema_fast.iloc[-1] < ema_slow.iloc[-1]:
        return "bear"
    return "range"
