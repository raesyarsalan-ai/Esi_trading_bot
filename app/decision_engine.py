def decide(signals):
    score = sum(signals.values())
    if score >= 2:
        return "buy"
    if score <= -2:
        return "sell"
