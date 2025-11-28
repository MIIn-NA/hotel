class Amenity:
    def __init__(self, name: str, description: str, cost: float):
        self.name = name
        self.description = description
        self.cost = cost

    def detailed_info(self) -> str:
        info = f"{self.name} - {self.description} (${self.cost})"
        words = [w.capitalize() for w in info.split()]
        return " ".join(words)

    def is_free(self) -> bool:
        return self.cost <= 0
