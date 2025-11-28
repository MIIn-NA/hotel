class Facility:
    def __init__(self, name: str, category: str, capacity: int):
        self.name = name
        self.category = category
        self.capacity = capacity

    def categorize(self) -> str:
        cat = self.category.lower()
        if "sport" in cat:
            return "Recreational"
        if "food" in cat:
            return "Dining"
        return "General"

    def is_large(self) -> bool:
        return self.capacity > 50
