class Treatment:
    def __init__(self, name: str, duration: int, price: float):
        self.name = name
        self.duration = duration
        self.price = price

    def final_price(self, discount: float) -> float:
        if discount < 0:
            return self.price
        return max(self.price - discount, 0)

    def is_long(self) -> bool:
        return self.duration >= 60
