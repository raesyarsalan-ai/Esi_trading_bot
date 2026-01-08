class ConfidenceFilter:
    def allow(self, confidence: float) -> bool:
        return confidence >= 0.6
