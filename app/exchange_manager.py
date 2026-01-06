import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

def get_exchange(name):
    exchange_class = getattr(ccxt, name)

    return exchange_class({
        "apiKey": os.getenv("API_KEY"),
        "secret": os.getenv("API_SECRET"),
        "enableRateLimit": True,
        "options": {"defaultType": "spot"}
    })
