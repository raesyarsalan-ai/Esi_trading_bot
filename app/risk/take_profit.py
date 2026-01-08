def take_profit(entry, side, rr):
    if side == "buy":
        return entry * (1 + rr)
    return entry * (1 - rr)
