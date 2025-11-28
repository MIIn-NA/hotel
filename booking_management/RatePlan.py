class RatePlan:
    def __init__(self, name: str, price: float, policy: str):
        self.name = name
        self.price = price
        self.policy = policy

    def calculate(self, nights: int) -> float:
        total = self.price * nights
        if "nonrefundable" in self.policy.lower():
            total *= 0.9
        return round(total, 2)

    def is_flexible(self) -> bool:
        return "flex" in self.policy.lower()
