class OrderValidator:
    def validate(self, symbol, side, amount):
        if amount <= 0:
            raise ValueError("Invalid order amount")
        if side not in ("buy", "sell"):
            raise ValueError("Invalid order side")
