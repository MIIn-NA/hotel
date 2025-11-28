class Analytics:
    def __init__(self, metric: str, value: float, label: str):
        self.metric = metric
        self.value = value
        self.label = label

    def upscale(self, factor: float) -> None:
        self.value *= max(factor, 0.1)

    def describe(self) -> str:
        return f"{self.metric} = {self.value} ({self.label})"
