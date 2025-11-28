class InventoryReport:
    def __init__(self, category: str, items_count: int, period: str):
        self.category = category
        self.items_count = items_count
        self.period = period

    def add_items(self, number: int) -> None:
        if number < 0:
            return
        self.items_count += number

    def summary(self) -> str:
        return f"{self.category}: {self.items_count} items ({self.period})"
