def stop_loss(entry, side, percent):
    if side == "buy":
        return entry * (1 - percent)
    return entry * (1 + percent)
