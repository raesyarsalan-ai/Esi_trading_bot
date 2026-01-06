DEFAULT_WEIGHTS = {
    "trend": 1.5,
    "range": 1.0,
    "ai": 2.0
}

def decide(signals, weights=None):
    if not signals:
        return None

    weights = weights or DEFAULT_WEIGHTS
    score = 0

    for key, value in signals.items():
        score += value * weights.get(key, 1)

    if score >= 2:
        return "buy"
    elif score <= -2:
        return "sell"
    return None
