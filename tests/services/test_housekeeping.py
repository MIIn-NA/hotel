import pytest
from services.Housekeeping import Housekeeping
from hotel_entities.Room import Room


class TestHousekeeping:
    def test_init(self):
        hk = Housekeeping("John Doe", "morning", "active")
        assert hk.staff_name == "John Doe"
        assert hk.shift == "morning"
        assert hk.status == "active"
        assert hk.rooms_cleaned == []

    def test_init_with_different_values(self):
        hk = Housekeeping("Jane Smith", "evening", "off-duty")
        assert hk.staff_name == "Jane Smith"
        assert hk.shift == "evening"
        assert hk.status == "off-duty"

    def test_init_empty_list(self):
        hk = Housekeeping("Staff", "night", "busy")
        assert hk.rooms_cleaned == []
        assert len(hk.rooms_cleaned) == 0

    def test_clean_room_valid(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room = Room(101, 1, True)
        hk.clean_room(room)
        assert len(hk.rooms_cleaned) == 1
        assert hk.rooms_cleaned[0] == room
        assert room.is_available is False

    def test_clean_room_sets_availability_to_false(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room = Room(101, 1, True)
        assert room.is_available is True
        hk.clean_room(room)
        assert room.is_available is False

    def test_clean_room_already_unavailable(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room = Room(101, 1, False)
        assert room.is_available is False
        hk.clean_room(room)
        assert room.is_available is False
        assert len(hk.rooms_cleaned) == 1

    def test_clean_multiple_rooms(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, True)
        room3 = Room(103, 1, True)
        hk.clean_room(room1)
        hk.clean_room(room2)
        hk.clean_room(room3)
        assert len(hk.rooms_cleaned) == 3
        assert room1.is_available is False
        assert room2.is_available is False
        assert room3.is_available is False

    def test_clean_room_invalid_type(self):
        hk = Housekeeping("John Doe", "morning", "active")
        with pytest.raises(ValueError, match="Invalid Room."):
            hk.clean_room("not a room")

    def test_clean_room_none(self):
        hk = Housekeeping("John Doe", "morning", "active")
        with pytest.raises(ValueError, match="Invalid Room."):
            hk.clean_room(None)

    def test_clean_room_invalid_object(self):
        hk = Housekeeping("John Doe", "morning", "active")
        with pytest.raises(ValueError, match="Invalid Room."):
            hk.clean_room({"number": 101})

    def test_clean_same_room_multiple_times(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room = Room(101, 1, True)
        hk.clean_room(room)
        hk.clean_room(room)
        assert len(hk.rooms_cleaned) == 2
        assert room.is_available is False

    def test_cleaned_count_empty(self):
        hk = Housekeeping("John Doe", "morning", "active")
        assert hk.cleaned_count() == 0

    def test_cleaned_count_single(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room = Room(101, 1, True)
        hk.clean_room(room)
        assert hk.cleaned_count() == 1

    def test_cleaned_count_multiple(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, True)
        room3 = Room(103, 1, True)
        hk.clean_room(room1)
        hk.clean_room(room2)
        hk.clean_room(room3)
        assert hk.cleaned_count() == 3

    def test_cleaned_count_consistency(self):
        hk = Housekeeping("John Doe", "morning", "active")
        assert hk.cleaned_count() == len(hk.rooms_cleaned)
        room = Room(101, 1, True)
        hk.clean_room(room)
        assert hk.cleaned_count() == len(hk.rooms_cleaned)

    def test_empty_string_parameters(self):
        hk = Housekeeping("", "", "")
        assert hk.staff_name == ""
        assert hk.shift == ""
        assert hk.status == ""

    def test_clean_rooms_from_different_floors(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room1 = Room(101, 1, True)
        room2 = Room(201, 2, True)
        room3 = Room(301, 3, True)
        hk.clean_room(room1)
        hk.clean_room(room2)
        hk.clean_room(room3)
        assert hk.cleaned_count() == 3
        assert all(not room.is_available for room in [room1, room2, room3])

    def test_room_availability_before_and_after_cleaning(self):
        hk = Housekeeping("John Doe", "morning", "active")
        room = Room(101, 1, True)
        initial_availability = room.is_available
        hk.clean_room(room)
        final_availability = room.is_available
        assert initial_availability is True
        assert final_availability is False

    def test_multiple_housekeepers_cleaning_same_room(self):
        hk1 = Housekeeping("John Doe", "morning", "active")
        hk2 = Housekeeping("Jane Smith", "evening", "active")
        room = Room(101, 1, True)
        hk1.clean_room(room)
        hk2.clean_room(room)
        assert hk1.cleaned_count() == 1
        assert hk2.cleaned_count() == 1
        assert room.is_available is False
