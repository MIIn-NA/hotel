class Forecast:
    def __init__(self, period: str, expected: float, label: str):
        self.period = period
        self.expected = expected
        self.label = label

    def adjust(self, delta: float) -> None:
        self.expected = max(0, self.expected + delta)

    def output(self) -> str:
        return f"{self.period}: {self.expected} ({self.label})"
