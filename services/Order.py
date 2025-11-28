from user_management.Guest import Guest
class Order:
    def __init__(self, order_id: str, total: float, status: str):
        self.order_id = order_id
        self.total = total
        self.status = status
        self.guest: Guest | None = None

    def assign_guest(self, guest: Guest) -> None:
        if not isinstance(guest, Guest):
            raise ValueError("Invalid Guest.")
        self.guest = guest
        if guest.vip:
            self.total *= 0.9

    def update_status(self, new_status: str) -> None:
        if len(new_status.strip()) < 3:
            raise ValueError("Status too short.")
        self.status = new_status.strip().upper()
