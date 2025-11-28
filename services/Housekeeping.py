from hotel_entities.Room import Room
class Housekeeping:
    def __init__(self, staff_name: str, shift: str, status: str):
        self.staff_name = staff_name
        self.shift = shift
        self.status = status
        self.rooms_cleaned: list[Room] = []

    def clean_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError("Invalid Room.")
        self.rooms_cleaned.append(room)
        room.is_available = False

    def cleaned_count(self) -> int:
        return len(self.rooms_cleaned)
