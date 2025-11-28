from user_management.Guest import Guest
class GuestReport:
    def __init__(self, period: str, vip_count: int, total_count: int):
        self.period = period
        self.vip_count = vip_count
        self.total_count = total_count
        self.guests: list[Guest] = []

    def add_guest(self, guest: Guest) -> None:
        if not isinstance(guest, Guest):
            raise ValueError("Invalid Guest.")
        self.guests.append(guest)
        self.total_count += 1
        if guest.vip:
            self.vip_count += 1

    def vip_ratio(self) -> float:
        if self.total_count == 0:
            return 0.0
        return round(self.vip_count / self.total_count, 3)
