import ccxt
from app.exchanges.base_exchange import BaseExchange

class CoinEx(BaseExchange):
    def __init__(self, api_key, secret, futures=False):
        options = {"defaultType": "swap" if futures else "spot"}
        client = ccxt.coinex({
            "apiKey": api_key,
            "secret": secret,
            "enableRateLimit": True,
            "options": options
        })
        super().__init__(client)

    def create_order(self, symbol, side, amount, price=None, params=None):
        params = params or {}
        if side == "buy":
            return self.client.create_market_buy_order(symbol, amount, params)
        return self.client.create_market_sell_order(symbol, amount, params)
