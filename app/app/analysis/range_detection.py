def is_range(df):
    high = df["high"].max()
    low = df["low"].min()
    return (high - low) / low < 0.01
