import time

from app.exchange_manager import get_exchange
from app.data_feed import fetch_ohlcv
from app.analysis.market_state import detect_market_state
from app.analysis.range_detection import is_range
from app.decision_engine import decide
from app.execution.executor import execute
from app.risk.drawdown_guard import DrawdownGuard
from app.risk.risk_manager import RiskManager
from app.ai.predictor import AIPredictor
from config.config import (
    EXCHANGE_NAME,
    SYMBOL,
    TIMEFRAME,
    ORDER_SIZE,
    MAX_DRAWDOWN,
    BASE_RISK,
)

def main():
    exchange = get_exchange(EXCHANGE_NAME)
    guard = DrawdownGuard(MAX_DRAWDOWN)
    risk = RiskManager(BASE_RISK)
    ai = AIPredictor(enabled=False)

    print("🚀 Trading bot started")

    while True:
        try:
            # ===== Market Data =====
            df = fetch_ohlcv(exchange, SYMBOL, TIMEFRAME)

            market = detect_market_state(df)
            range_market = is_range(df)

            ai_signal = ai.predict({
                "market": market,
                "range": range_market
            })

            signals = {
                "trend": 1 if market == "bull" else -1,
                "range": -1 if range_market else 1,
                "ai": ai_signal
            }

            decision = decide(signals)

            # ===== Balance =====
            balance_info = exchange.fetch_balance()
            balance = balance_info["free"].get("USDT", 0)

            # ===== Risk Guard =====
            if not guard.allow(balance):
                print("⛔ Drawdown limit reached")
                time.sleep(60)
                continue

            # ===== Execute =====
            if decision:
                execute(exchange, decision, SYMBOL, ORDER_SIZE)
                print(f"[TRADE] {decision.upper()} executed")

        except Exception as e:
            print(f"[MAIN ERROR] {e}")

        time.sleep(60)

if __name__ == "__main__":
    main()
