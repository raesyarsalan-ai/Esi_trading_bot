def execute(exchange, side, symbol, amount):
    if side == "buy":
        exchange.create_market_buy_order(symbol, amount)
    if side == "sell":
        exchange.create_market_sell_order(symbol, amount)
