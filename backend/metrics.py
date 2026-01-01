import time

class Metrics:
    def __init__(self):
        self.requests = 0
        self.fallbacks = 0
        self.latency = 0

    def start(self):
        return time.time()

    def end(self, s):
        self.latency += time.time() - s

    def stats(self):
        avg_latency = round(self.latency / max(1, self.requests), 3)
        fallback_rate = round(self.fallbacks / max(1, self.requests), 2)

        return {
            "avg_latency_sec": avg_latency,
            "fallback_rate": fallback_rate,
            "cost": "$0 (offline NLP)",
            "reliability": "High"
        }

metrics = Metrics()
