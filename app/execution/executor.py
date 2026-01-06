def execute(exchange, side, symbol, amount):
    try:
        if side == "buy":
            return exchange.create_market_buy_order(symbol, amount)
        elif side == "sell":
            return exchange.create_market_sell_order(symbol, amount)
    except Exception as e:
        print(f"[EXECUTION ERROR] {e}")
