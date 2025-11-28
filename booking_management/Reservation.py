from user_management.Guest import Guest
from hotel_entities.Room import Room
class Reservation:
    def __init__(self, code: str, guest_id: str, room_number: int):
        self.code = code
        self.guest_id = guest_id
        self.room_number = room_number
        self.guest: Guest | None = None
        self.room: Room | None = None

    def assign_guest(self, guest: Guest) -> None:
        if not isinstance(guest, Guest):
            raise ValueError("Invalid Guest instance.")
        self.guest = guest
        if hasattr(guest, "name"):
            self.guest_id = guest.name.lower().replace(" ", "_")

    def assign_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError("Expected Room instance.")
        self.room = room
        self.room_number = room.number
