import time
from config.config import *
from exchange.coinex import get_exchange
from strategies.strategy_engine import decide_trade
from risk.risk_manager import RiskManager

def main():
    print("🚀 Trading bot started")

    exchange = get_exchange()
    risk = RiskManager(
        max_drawdown=MAX_DRAWDOWN,
        base_risk=BASE_RISK
    )

    while True:
        try:
            # 1️⃣ دریافت موجودی
            balance_info = exchange.fetch_balance()
            balance = balance_info["free"].get("USDT", 0)

            if balance <= 0:
                print("⚠️ No USDT balance")
                time.sleep(30)
                continue

            # 2️⃣ تصمیم‌گیری استراتژی
            decision = decide_trade(exchange)

            if decision == "hold":
                print("⏸ No trade signal")
                time.sleep(30)
                continue

            # 3️⃣ قیمت بازار
            ticker = exchange.fetch_ticker(SYMBOL)
            last_price = ticker["last"]

            # 4️⃣ محاسبه حجم معامله
            size = risk.get_position_size(
                balance,
                last_price,
                STOP_LOSS_PERCENT
            )

            if size <= 0:
                print("⚠️ Invalid position size")
                time.sleep(30)
                continue

            # 5️⃣ ارسال سفارش
            print(f"📈 Executing {decision.upper()} | size={size}")

            if decision == "buy":
                exchange.create_market_buy_order(SYMBOL, size)
            elif decision == "sell":
                exchange.create_market_sell_order(SYMBOL, size)

            time.sleep(60)

        except Exception as e:
            print(f"[MAIN ERROR] {e}")
            time.sleep(30)

if __name__ == "__main__":
    main()
