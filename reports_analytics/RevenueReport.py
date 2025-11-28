class RevenueReport:
    def __init__(self, category: str, revenue: float, period: str):
        self.category = category
        self.revenue = revenue
        self.period = period

    def adjust(self, amount: float) -> None:
        self.revenue += amount
        if self.revenue < 0:
            self.revenue = 0

    def detail(self) -> str:
        return f"{self.category}: {self.revenue} ({self.period})"
