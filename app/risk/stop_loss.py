def stop_loss(entry, percent):
    return entry * (1 - percent)

def trailing_stop(entry, current_price, trail_percent):
    if current_price > entry:
        return current_price * (1 - trail_percent)
    return stop_loss(entry, trail_percent)
