import time
from exchange_manager import get_exchange
from data_feed import fetch_ohlcv
from analysis.market_state import detect_market_state
from analysis.range_detection import is_range
from strategies.trend import trend_follow
from decision_engine import decide
from execution.executor import execute
from risk.drawdown_guard import DrawdownGuard
from config.config import *

exchange = get_exchange(EXCHANGE_NAME)
guard = DrawdownGuard(MAX_DRAWDOWN)

while True:
    df = fetch_ohlcv(exchange, SYMBOL, TIMEFRAME)
    market = detect_market_state(df)
    range_market = is_range(df)

    signals = {
        "trend": 1 if market == "bull" else -1,
        "range": -1 if range_market else 1
    }

    decision = decide(signals)
    balance = exchange.fetch_balance()["total"]["USDT"]

    if decision and guard.allow(balance):
        execute(exchange, decision, SYMBOL, ORDER_SIZE)

    time.sleep(60)
