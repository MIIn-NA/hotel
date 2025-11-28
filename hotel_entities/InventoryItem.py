class InventoryItem:
    def __init__(self, name: str, quantity: int, code: str):
        self.name = name
        self.quantity = quantity
        self.code = code

    def use(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if amount > self.quantity:
            self.quantity = 0
        else:
            self.quantity -= amount

    def restock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Invalid restock amount.")
        self.quantity += amount
