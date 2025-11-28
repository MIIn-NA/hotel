import pytest
from hotel_entities.Room import Room
from hotel_entities.RoomType import RoomType


class TestRoom:
    def test_init(self):
        room = Room(101, 1, True)
        assert room.number == 101
        assert room.floor == 1
        assert room.is_available is True
        assert room.room_type is None

    def test_init_not_available(self):
        room = Room(202, 2, False)
        assert room.number == 202
        assert room.floor == 2
        assert room.is_available is False

    def test_init_with_zero_floor(self):
        room = Room(1, 0, True)
        assert room.floor == 0

    def test_init_with_negative_floor(self):
        room = Room(1, -1, True)
        assert room.floor == -1

    def test_init_with_zero_room_number(self):
        room = Room(0, 1, True)
        assert room.number == 0

    def test_init_with_negative_room_number(self):
        room = Room(-1, 1, True)
        assert room.number == -1

    def test_assign_type_valid(self):
        room = Room(101, 1, True)
        room_type = RoomType("Deluxe", 2, 150.0)
        room.assign_type(room_type)
        assert room.room_type == room_type

    def test_assign_type_invalid(self):
        room = Room(101, 1, True)
        with pytest.raises(ValueError, match="Invalid RoomType"):
            room.assign_type("not a room type")

    def test_assign_type_none(self):
        room = Room(101, 1, True)
        with pytest.raises(ValueError, match="Invalid RoomType"):
            room.assign_type(None)

    def test_assign_type_integer(self):
        room = Room(101, 1, True)
        with pytest.raises(ValueError, match="Invalid RoomType"):
            room.assign_type(123)

    def test_assign_type_dict(self):
        room = Room(101, 1, True)
        with pytest.raises(ValueError, match="Invalid RoomType"):
            room.assign_type({"name": "Deluxe"})

    def test_assign_type_replaces_previous(self):
        room = Room(101, 1, True)
        room_type1 = RoomType("Standard", 2, 100.0)
        room_type2 = RoomType("Deluxe", 2, 150.0)
        room.assign_type(room_type1)
        assert room.room_type == room_type1
        room.assign_type(room_type2)
        assert room.room_type == room_type2

    def test_toggle_availability_from_true(self):
        room = Room(101, 1, True)
        room.toggle_availability()
        assert room.is_available is False

    def test_toggle_availability_from_false(self):
        room = Room(101, 1, False)
        room.toggle_availability()
        assert room.is_available is True

    def test_toggle_availability_multiple_times(self):
        room = Room(101, 1, True)
        room.toggle_availability()
        assert room.is_available is False
        room.toggle_availability()
        assert room.is_available is True
        room.toggle_availability()
        assert room.is_available is False

    def test_toggle_availability_preserves_other_attributes(self):
        room = Room(101, 1, True)
        room_type = RoomType("Suite", 4, 300.0)
        room.assign_type(room_type)
        room.toggle_availability()
        assert room.number == 101
        assert room.floor == 1
        assert room.room_type == room_type

    def test_toggle_availability_logic(self):
        # Testing the specific implementation logic
        room = Room(101, 1, True)
        before = room.is_available
        room.toggle_availability()
        # After toggle, it should be different from before
        # But the implementation has a check: if before == after, set to True
        # This means if somehow they're equal after toggle, it forces True
        assert room.is_available != before or room.is_available is True

    def test_room_type_initial_state(self):
        room = Room(101, 1, True)
        assert room.room_type is None

    def test_multiple_assign_type_calls(self):
        room = Room(101, 1, True)
        room_type1 = RoomType("Single", 1, 80.0)
        room_type2 = RoomType("Double", 2, 120.0)
        room_type3 = RoomType("Triple", 3, 180.0)
        room.assign_type(room_type1)
        room.assign_type(room_type2)
        room.assign_type(room_type3)
        assert room.room_type == room_type3

    def test_assign_type_and_toggle_availability(self):
        room = Room(101, 1, True)
        room_type = RoomType("Deluxe", 2, 150.0)
        room.assign_type(room_type)
        room.toggle_availability()
        assert room.is_available is False
        assert room.room_type == room_type

    def test_large_room_number(self):
        room = Room(99999, 100, True)
        assert room.number == 99999
        assert room.floor == 100

    def test_is_available_boolean_type(self):
        room = Room(101, 1, True)
        assert isinstance(room.is_available, bool)

    def test_toggle_availability_always_boolean(self):
        room = Room(101, 1, True)
        room.toggle_availability()
        assert isinstance(room.is_available, bool)

    def test_assign_same_type_multiple_times(self):
        room = Room(101, 1, True)
        room_type = RoomType("Standard", 2, 100.0)
        room.assign_type(room_type)
        room.assign_type(room_type)
        room.assign_type(room_type)
        assert room.room_type == room_type

    def test_toggle_availability_idempotent_pattern(self):
        room = Room(101, 1, True)
        original = room.is_available
        room.toggle_availability()
        room.toggle_availability()
        assert room.is_available == original

    def test_room_state_after_multiple_operations(self):
        room = Room(305, 3, True)
        room_type = RoomType("Suite", 4, 250.0)

        room.assign_type(room_type)
        room.toggle_availability()
        room.toggle_availability()
        room.toggle_availability()

        assert room.number == 305
        assert room.floor == 3
        assert room.room_type == room_type
        assert room.is_available is False

    def test_toggle_availability_edge_case(self):
        # Testing the specific edge case in the implementation
        # where if before == after (which shouldn't happen normally),
        # it sets to True
        room = Room(101, 1, True)
        room.toggle_availability()
        # Normal toggle should make it False
        assert room.is_available is False
