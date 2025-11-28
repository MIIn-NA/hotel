from user_management.Guest import Guest
class CheckOut:
    def __init__(self, date: str, time: str, report: str):
        self.date = date
        self.time = time
        self.report = report
        self.guest: Guest | None = None

    def assign_guest(self, guest: Guest) -> None:
        if not isinstance(guest, Guest):
            raise ValueError("Invalid Guest instance.")
        self.guest = guest

    def generate_report(self) -> str:
        text = f"{self.date} {self.time}: {self.report}"
        if self.guest:
            text += f" by {self.guest.name}"
        lines = [word.capitalize() for word in text.split()]
        return " ".join(lines)
