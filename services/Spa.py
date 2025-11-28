from services.Treatment import Treatment
class Spa:
    def __init__(self, name: str, area: int, rating: int):
        self.name = name
        self.area = area
        self.rating = rating
        self.treatments: list[Treatment] = []

    def add_treatment(self, treatment: Treatment) -> None:
        if not isinstance(treatment, Treatment):
            raise ValueError("Invalid treatment.")
        self.treatments.append(treatment)
        self.rating = min(10, self.rating + 1)

    def treatment_count(self) -> int:
        return len(self.treatments)
