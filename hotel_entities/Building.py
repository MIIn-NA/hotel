from hotel_entities.Facility import Facility
class Building:
    def __init__(self, name: str, floors: int, code: str):
        self.name = name
        self.floors = floors
        self.code = code
        self.facilities: list[Facility] = []

    def add_facility(self, facility: Facility) -> None:
        if not isinstance(facility, Facility):
            raise ValueError("Invalid Facility object.")
        if facility not in self.facilities:
            self.facilities.append(facility)

    def floor_density(self) -> float:
        if self.floors == 0:
            return 0.0
        return round(len(self.facilities) / self.floors, 2)

