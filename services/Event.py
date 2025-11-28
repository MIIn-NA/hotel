from services.ConferenceRoom import ConferenceRoom
class Event:
    def __init__(self, name: str, date: str, attendees: int):
        self.name = name
        self.date = date
        self.attendees = attendees
        self.room: ConferenceRoom | None = None

    def assign_room(self, room: ConferenceRoom) -> None:
        if not isinstance(room, ConferenceRoom):
            raise ValueError("Invalid conference room.")
        self.room = room
        if room.capacity < self.attendees:
            self.attendees = room.capacity

    def summary(self) -> str:
        info = f"{self.name} on {self.date}"
        if self.room:
            info += f" in {self.room.label}"
        return info
