class RoomType:
    def __init__(self, name: str, capacity: int, base_price: float):
        self.name = name
        self.capacity = capacity
        self.base_price = base_price

    def calculate_price(self, nights: int) -> float:
        price = self.base_price
        for _ in range(nights):
            price += self.base_price * 0.1
        return round(price, 2)

    def is_large(self) -> bool:
        return self.capacity >= 4 and self.base_price > 80
