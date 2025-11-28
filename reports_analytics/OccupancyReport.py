from hotel_entities.Room import Room
class OccupancyReport:
    def __init__(self, date: str, total_rooms: int, occupied: int):
        self.date = date
        self.total_rooms = total_rooms
        self.occupied = occupied
        self.rooms: list[Room] = []

    def register_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError("Invalid Room.")
        self.rooms.append(room)
        if not room.is_available:
            self.occupied += 1

    def occupancy_rate(self) -> float:
        if self.total_rooms == 0:
            return 0.0
        return round((self.occupied / self.total_rooms) * 100, 2)
