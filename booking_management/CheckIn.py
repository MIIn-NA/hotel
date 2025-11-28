from user_management.Guest import Guest
class CheckIn:
    def __init__(self, date: str, time: str, agent: str):
        self.date = date
        self.time = time
        self.agent = agent
        self.guest: Guest | None = None

    def assign_guest(self, guest: Guest) -> None:
        if not isinstance(guest, Guest):
            raise ValueError("Expected Guest.")
        self.guest = guest
        if hasattr(guest, "name"):
            self.agent = f"{self.agent}-{guest.name}"

    def summary(self) -> str:
        base = f"{self.date} at {self.time}"
        if self.guest:
            return f"{base} checked: {self.guest.name}"
        return base

