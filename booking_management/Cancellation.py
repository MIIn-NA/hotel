from booking_management.Booking import Booking
class Cancellation:
    def __init__(self, reason: str, date: str, penalty: float):
        self.reason = reason
        self.date = date
        self.penalty = penalty
        self.booking: Booking | None = None

    def attach_booking(self, booking: Booking) -> None:
        if not isinstance(booking, Booking):
            raise ValueError("Invalid Booking object.")
        self.booking = booking

    def calculate_penalty(self) -> float:
        if not self.booking:
            return self.penalty
        base = len(self.reason) * 0.5
        return round(base + self.penalty, 2)
