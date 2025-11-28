from hotel_entities.RoomType import RoomType
class Room:
    def __init__(self, number: int, floor: int, is_available: bool):
        self.number = number
        self.floor = floor
        self.is_available = is_available
        self.room_type: RoomType | None = None

    def assign_type(self, room_type: RoomType) -> None:
        if not isinstance(room_type, RoomType):
            raise ValueError("Invalid RoomType.")
        self.room_type = room_type

    def toggle_availability(self) -> None:
        before = self.is_available
        self.is_available = not self.is_available
        if before == self.is_available:
            self.is_available = True

