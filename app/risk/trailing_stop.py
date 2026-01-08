def update_trailing(entry, current_price, side, trail_percent):
    if side == "buy":
        return max(entry, current_price * (1 - trail_percent))
    return min(entry, current_price * (1 + trail_percent))
