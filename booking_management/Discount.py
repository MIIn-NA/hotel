class Discount:
    def __init__(self, code: str, amount: float, description: str):
        self.code = code
        self.amount = amount
        self.description = description

    def apply(self, total: float) -> float:
        if self.amount < 0:
            return total
        new_total = total - self.amount
        return max(new_total, 0)

    def is_valid(self) -> bool:
        return len(self.code) >= 3 and self.amount >= 0
