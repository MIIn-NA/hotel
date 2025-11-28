from hotel_entities.Room import Room
class Floor:
    def __init__(self, number: int, label: str, accessible: bool):
        self.number = number
        self.label = label
        self.accessible = accessible
        self.rooms: list[Room] = []

    def add_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError("Expected Room instance.")
        self.rooms.append(room)
        self.rooms.sort(key=lambda r: r.number)

    def count_available(self) -> int:
        count = 0
        for room in self.rooms:
            if room.is_available:
                count += 1
        return count
