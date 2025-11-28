import pytest
from booking_management.Reservation import Reservation
from user_management.Guest import Guest
from hotel_entities.Room import Room


class TestReservation:
    def test_init(self):
        res = Reservation("R001", "guest123", 101)
        assert res.code == "R001"
        assert res.guest_id == "guest123"
        assert res.room_number == 101
        assert res.guest is None
        assert res.room is None

    def test_assign_guest_valid(self):
        res = Reservation("R001", "guest123", 101)
        guest = Guest("John Doe", "jdoe", False)
        res.assign_guest(guest)
        assert res.guest == guest
        assert res.guest_id == "john_doe"

    def test_assign_guest_invalid_type(self):
        res = Reservation("R001", "guest123", 101)
        with pytest.raises(ValueError, match="Invalid Guest instance"):
            res.assign_guest("not a guest")

    def test_assign_guest_name_transformation(self):
        res = Reservation("R001", "guest123", 101)
        guest = Guest("Alice Smith", "asmith", True)
        res.assign_guest(guest)
        assert res.guest_id == "alice_smith"

    def test_assign_guest_without_name_attribute(self):
        res = Reservation("R001", "guest123", 101)
        guest = Guest("Bob", "bob123", False)
        delattr(guest, "name")
        res.assign_guest(guest)
        assert res.guest_id == "guest123"

    def test_assign_room_valid(self):
        res = Reservation("R001", "guest123", 101)
        room = Room(201, 2, True)
        res.assign_room(room)
        assert res.room == room
        assert res.room_number == 201

    def test_assign_room_invalid_type(self):
        res = Reservation("R001", "guest123", 101)
        with pytest.raises(ValueError, match="Expected Room instance"):
            res.assign_room("not a room")

    def test_assign_room_updates_room_number(self):
        res = Reservation("R001", "guest123", 101)
        room = Room(305, 3, True)
        res.assign_room(room)
        assert res.room_number == 305

    def test_full_assignment(self):
        res = Reservation("R001", "guest123", 101)
        guest = Guest("Jane Doe", "jdoe", True)
        room = Room(202, 2, True)
        res.assign_guest(guest)
        res.assign_room(room)
        assert res.guest == guest
        assert res.room == room
        assert res.guest_id == "jane_doe"
        assert res.room_number == 202
