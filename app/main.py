import time

from app.exchange_manager import get_exchange
from app.data_feed import fetch_ohlcv
from app.analysis.market_analysis import detect_market_state, is_range
from app.decision_engine import decide
from app.execution.executor import execute
from app.risk.drawdown_guard import DrawdownGuard
from app.risk.risk_manager import RiskManager
from app.ai.predictor import AIPredictor
from app.state import TradeState
from config.config import *

def main():
    exchange = get_exchange(EXCHANGE_NAME)
    guard = DrawdownGuard(MAX_DRAWDOWN)
    risk = RiskManager(BASE_RISK)
    ai = AIPredictor(enabled=False)
    state = TradeState()

    print("🚀 Trading bot started")

    while True:
        try:
            df = fetch_ohlcv(exchange, SYMBOL, TIMEFRAME)
            market = detect_market_state(df)
            range_market = is_range(df)

            last_price = df["close"].iloc[-1]
            balance_info = exchange.fetch_balance()
balance = balance_info["free"].get("USDT", 0)

           

            if not guard.allow(balance):
                print("⛔ Drawdown limit reached")
                time.sleep(60)
                continue

            ai_signal = ai.predict({
                "market": market,
                "range": range_market
            })

            signals = {
                "trend": 1 if market == "bull" else -1,
                "range": 1 if range_market else -1,
                "ai": ai_signal
            }

            decision = decide(signals)

            if decision and not state.in_position:
                size = risk.get_position_size(balance, last_price, STOP_LOSS_PERCENT)
                if size > 0:
                    execute(exchange, decision, SYMBOL, size)
                    state.in_position = True
                    print(f"[TRADE] {decision.upper()} | size={size}")

        except Exception as e:
            print(f"[MAIN ERROR] {e}")

        time.sleep(60)

if __name__ == "__main__":
    main()
