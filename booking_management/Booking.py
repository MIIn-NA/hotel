from booking_management.Reservation import Reservation
class Booking:
    def __init__(self, booking_id: str, nights: int, status: str):
        self.booking_id = booking_id
        self.nights = nights
        self.status = status
        self.reservations: list[Reservation] = []

    def add_reservation(self, reservation: Reservation) -> None:
        if not isinstance(reservation, Reservation):
            raise ValueError("Only Reservation allowed.")
        if reservation not in self.reservations:
            self.reservations.append(reservation)

    def total_rooms(self) -> int:
        count = 0
        for r in self.reservations:
            if r.room is not None:
                count += 1
        return count
