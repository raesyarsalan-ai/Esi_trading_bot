class RiskEngine:
    def __init__(self, max_risk):
        self.max_risk = max_risk

    def approve(self, confidence):
        return confidence * self.max_risk
