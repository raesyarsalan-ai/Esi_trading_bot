def is_pin_bar(df):
    if len(df) < 1:
        return False

    c = df.iloc[-1]
    body = abs(c.close - c.open)
    wick = c.high - max(c.close, c.open)

    return body > 0 and wick > body * 2
