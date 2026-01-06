def calculate_size(balance, risk, stop_distance):
    if stop_distance <= 0:
        return 0
    return (balance * risk) / stop_distance
