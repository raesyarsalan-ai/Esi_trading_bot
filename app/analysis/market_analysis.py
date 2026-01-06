import ta

def detect_market_state(df):
    if len(df) < 50:
        return "range"

    ema_fast = ta.trend.ema_indicator(df["close"], 20)
    ema_slow = ta.trend.ema_indicator(df["close"], 50)

    if ema_fast.iloc[-1] > ema_slow.iloc[-1]:
        return "bull"
    elif ema_fast.iloc[-1] < ema_slow.iloc[-1]:
        return "bear"
    return "range"


def is_range(df):
    if len(df) < 20:
        return True

    high = df["high"].max()
    low = df["low"].min()

    if low == 0:
        return False

    return (high - low) / low < 0.01
