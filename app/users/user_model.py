from dataclasses import dataclass

@dataclass
class User:
    user_id: str
    is_admin: bool = False
    is_active: bool = False
    subscription_plan: str | None = None

    def can_trade(self) -> bool:
        if self.is_admin:
            return True
        return self.is_active and self.subscription_plan is not None
