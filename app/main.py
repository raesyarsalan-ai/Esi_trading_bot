from app.core.session_manager import SessionManager
from app.core.bot_engine import BotEngine
from app.execution.order_executor import OrderExecutor
from app.exchanges.coinex import CoinEx
from app.security.key_manager import APIKeyManager

def main():
    session = SessionManager()
    user = session.create_user("admin")  # ادمین بدون پرداخت

    key_manager = APIKeyManager()
    key_manager.save_keys(user.user_id, "API_KEY", "SECRET")

    keys = key_manager.load_keys(user.user_id)

    exchange = CoinEx(
        api_key=keys["api_key"],
        secret=keys["secret"],
        futures=True
    )

    executor = OrderExecutor(exchange)
    engine = BotEngine(user, exchange, executor)

    engine.trade("buy", "BTC/USDT", 0.001)
    print("✅ Trade executed")

if __name__ == "__main__":
    main()
