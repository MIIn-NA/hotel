from hotel_entities.Floor import Floor
from hotel_entities.Location import Location
class Hotel:
    def __init__(self, name: str, rating: int, address: str):
        self.name = name
        self.rating = rating
        self.address = address
        self.floors: list[Floor] = []
        self.location: Location | None = None

    def add_floor(self, floor: Floor) -> None:
        if not isinstance(floor, Floor):
            raise ValueError("Only Floor instances allowed.")
        if floor in self.floors:
            return
        self.floors.append(floor)
        self.floors.sort(key=lambda f: f.number)

    def set_location(self, location: Location) -> None:
        if not isinstance(location, Location):
            raise ValueError("Invalid location object.")
        self.location = location
        if hasattr(location, "city"):
            self.address = f"{location.city}, {self.address}"
