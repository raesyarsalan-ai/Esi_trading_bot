def is_range(df):
    if len(df) < 20:
        return True

    high = df["high"].max()
    low = df["low"].min()

    if low == 0:
        return False

    return (high - low) / low < 0.01
