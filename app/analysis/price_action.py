def is_pin_bar(df):
    c = df.iloc[-1]
    body = abs(c.close - c.open)
    wick = c.high - max(c.close, c.open)
    return wick > body * 2
