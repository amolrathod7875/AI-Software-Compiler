from typing import Dict, Any

class MetricsTracker:
    def __init__(self):
        self.success_rate = 0.0
        self.retries = 0
        self.latency = 0.0
        self.cost = 0.0

    def record(self, success: bool, latency: float, cost: float = 0.0):
        self.retries += 1 if not success else 0
        # Update running average
        total = self.retries + 1
        self.success_rate = (self.success_rate * (total - 1) + (1 if success else 0)) / total
        self.latency = latency
        self.cost += cost