from dataclasses import dataclass
import os

@dataclass
class Settings:
    ENV: str = os.getenv("ENV", "production")

    # ===== Admin =====
    ADMIN_USER_ID: str = os.getenv("ADMIN_USER_ID", "admin")

    # ===== Trading =====
    DEFAULT_TIMEFRAME: str = "5m"
    MAX_DRAWDOWN: float = 0.2
    BASE_RISK: float = 0.01

    # ===== Exchanges =====
    ALLOWED_EXCHANGES = ["coinex", "mexc", "gate"]
    ENABLE_FUTURES: bool = True

    # ===== Security =====
    ENCRYPTION_KEY: str = os.getenv("ENCRYPTION_KEY", "CHANGE_ME")

settings = Settings()
