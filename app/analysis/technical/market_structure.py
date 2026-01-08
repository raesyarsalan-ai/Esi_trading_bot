def market_structure(df):
    highs = df["high"].tail(5)
    lows = df["low"].tail(5)

    if highs.is_monotonic_increasing and lows.is_monotonic_increasing:
        return "higher_highs"
    if highs.is_monotonic_decreasing and lows.is_monotonic_decreasing:
        return "lower_lows"
    return "range"
