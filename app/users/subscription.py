class SubscriptionService:
    def __init__(self):
        self.plans = {
            "basic": {"max_pairs": 1},
            "pro": {"max_pairs": 5},
            "premium": {"max_pairs": 20},
        }

    def validate(self, user):
        return user.can_trade()
