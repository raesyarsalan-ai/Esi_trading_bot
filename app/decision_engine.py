from app.knowledge.trading_book import TRADING_BOOK

DEFAULT_WEIGHTS = {
    "trend": 1.5,
    "range": 1.0,
    "scalping": 1.0,
    "intraday": 1.2,
    "swing": 1.3,
    "ai": 2.0
}

def decide(signals: dict, weights: dict = None):
    """
    Professional decision engine with weighted signals
    Backward compatible with old logic
    """
    if not signals:
        return None

    weights = weights or DEFAULT_WEIGHTS

    score = 0
    for name, value in signals.items():
        score += value * weights.get(name, 1)

    if score >= 2:
        return "buy"
    elif score <= -2:
        return "sell"
    return None
