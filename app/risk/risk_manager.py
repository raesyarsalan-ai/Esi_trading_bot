from app.risk.position_sizing import calculate_size
from app.risk.stop_loss import stop_loss

class RiskManager:
    def __init__(self, base_risk):
        self.base_risk = base_risk

    def get_position_size(self, balance, entry, stop_percent):
        stop_price = stop_loss(entry, stop_percent)
        distance = abs(entry - stop_price)
        return calculate_size(balance, self.base_risk, distance)
