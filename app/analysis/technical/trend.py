def trend(indicators):
    if indicators["ema_fast"] > indicators["ema_slow"]:
        return "bull"
    if indicators["ema_fast"] < indicators["ema_slow"]:
        return "bear"
    return "neutral"
