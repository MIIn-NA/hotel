import pytest
from booking_management.Booking import Booking
from booking_management.Reservation import Reservation


class TestBooking:
    def test_init(self):
        booking = Booking("BK123", 3, "confirmed")
        assert booking.booking_id == "BK123"
        assert booking.nights == 3
        assert booking.status == "confirmed"
        assert booking.reservations == []

    def test_add_reservation_valid(self):
        booking = Booking("BK123", 3, "confirmed")
        reservation = Reservation("R001", "guest1", 101)
        booking.add_reservation(reservation)
        assert len(booking.reservations) == 1
        assert booking.reservations[0] == reservation

    def test_add_reservation_duplicate(self):
        booking = Booking("BK123", 3, "confirmed")
        reservation = Reservation("R001", "guest1", 101)
        booking.add_reservation(reservation)
        booking.add_reservation(reservation)
        assert len(booking.reservations) == 1

    def test_add_reservation_invalid_type(self):
        booking = Booking("BK123", 3, "confirmed")
        with pytest.raises(ValueError, match="Only Reservation allowed"):
            booking.add_reservation("not a reservation")

    def test_add_multiple_reservations(self):
        booking = Booking("BK123", 3, "confirmed")
        res1 = Reservation("R001", "guest1", 101)
        res2 = Reservation("R002", "guest2", 102)
        booking.add_reservation(res1)
        booking.add_reservation(res2)
        assert len(booking.reservations) == 2

    def test_total_rooms_no_reservations(self):
        booking = Booking("BK123", 3, "confirmed")
        assert booking.total_rooms() == 0

    def test_total_rooms_with_assigned_rooms(self):
        from hotel_entities.Room import Room
        booking = Booking("BK123", 3, "confirmed")
        res1 = Reservation("R001", "guest1", 101)
        res2 = Reservation("R002", "guest2", 102)
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, True)
        res1.room = room1
        res2.room = room2
        booking.add_reservation(res1)
        booking.add_reservation(res2)
        assert booking.total_rooms() == 2

    def test_total_rooms_without_assigned_rooms(self):
        booking = Booking("BK123", 3, "confirmed")
        res1 = Reservation("R001", "guest1", 101)
        res2 = Reservation("R002", "guest2", 102)
        booking.add_reservation(res1)
        booking.add_reservation(res2)
        assert booking.total_rooms() == 0

    def test_total_rooms_mixed(self):
        from hotel_entities.Room import Room
        booking = Booking("BK123", 3, "confirmed")
        res1 = Reservation("R001", "guest1", 101)
        res2 = Reservation("R002", "guest2", 102)
        room1 = Room(101, 1, True)
        res1.room = room1
        booking.add_reservation(res1)
        booking.add_reservation(res2)
        assert booking.total_rooms() == 1
