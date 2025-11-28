import pytest
from hotel_entities.Floor import Floor
from hotel_entities.Room import Room


class TestFloor:
    def test_init(self):
        floor = Floor(1, "Ground Floor", True)
        assert floor.number == 1
        assert floor.label == "Ground Floor"
        assert floor.accessible is True
        assert floor.rooms == []

    def test_init_not_accessible(self):
        floor = Floor(5, "Fifth Floor", False)
        assert floor.number == 5
        assert floor.label == "Fifth Floor"
        assert floor.accessible is False

    def test_init_negative_number(self):
        floor = Floor(-1, "Basement", True)
        assert floor.number == -1

    def test_init_zero_number(self):
        floor = Floor(0, "Lobby", True)
        assert floor.number == 0

    def test_init_with_empty_label(self):
        floor = Floor(3, "", True)
        assert floor.label == ""

    def test_add_room_valid(self):
        floor = Floor(1, "First Floor", True)
        room = Room(101, 1, True)
        floor.add_room(room)
        assert len(floor.rooms) == 1
        assert floor.rooms[0] == room

    def test_add_room_invalid_type(self):
        floor = Floor(1, "First Floor", True)
        with pytest.raises(ValueError, match="Expected Room instance"):
            floor.add_room("not a room")

    def test_add_room_none(self):
        floor = Floor(1, "First Floor", True)
        with pytest.raises(ValueError, match="Expected Room instance"):
            floor.add_room(None)

    def test_add_room_integer(self):
        floor = Floor(1, "First Floor", True)
        with pytest.raises(ValueError, match="Expected Room instance"):
            floor.add_room(101)

    def test_add_room_dict(self):
        floor = Floor(1, "First Floor", True)
        with pytest.raises(ValueError, match="Expected Room instance"):
            floor.add_room({"number": 101})

    def test_add_multiple_rooms(self):
        floor = Floor(1, "First Floor", True)
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, True)
        room3 = Room(103, 1, False)
        floor.add_room(room1)
        floor.add_room(room2)
        floor.add_room(room3)
        assert len(floor.rooms) == 3

    def test_add_room_sorting(self):
        floor = Floor(1, "First Floor", True)
        room3 = Room(103, 1, True)
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, True)
        floor.add_room(room3)
        floor.add_room(room1)
        floor.add_room(room2)
        assert floor.rooms[0].number == 101
        assert floor.rooms[1].number == 102
        assert floor.rooms[2].number == 103

    def test_add_room_already_sorted(self):
        floor = Floor(1, "First Floor", True)
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, True)
        room3 = Room(103, 1, True)
        floor.add_room(room1)
        floor.add_room(room2)
        floor.add_room(room3)
        assert floor.rooms[0].number == 101
        assert floor.rooms[1].number == 102
        assert floor.rooms[2].number == 103

    def test_add_room_reverse_order(self):
        floor = Floor(1, "First Floor", True)
        room5 = Room(105, 1, True)
        room4 = Room(104, 1, True)
        room3 = Room(103, 1, True)
        room2 = Room(102, 1, True)
        room1 = Room(101, 1, True)
        floor.add_room(room5)
        floor.add_room(room4)
        floor.add_room(room3)
        floor.add_room(room2)
        floor.add_room(room1)
        assert floor.rooms[0].number == 101
        assert floor.rooms[4].number == 105

    def test_count_available_no_rooms(self):
        floor = Floor(1, "First Floor", True)
        assert floor.count_available() == 0

    def test_count_available_all_available(self):
        floor = Floor(1, "First Floor", True)
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, True)
        room3 = Room(103, 1, True)
        floor.add_room(room1)
        floor.add_room(room2)
        floor.add_room(room3)
        assert floor.count_available() == 3

    def test_count_available_none_available(self):
        floor = Floor(1, "First Floor", True)
        room1 = Room(101, 1, False)
        room2 = Room(102, 1, False)
        room3 = Room(103, 1, False)
        floor.add_room(room1)
        floor.add_room(room2)
        floor.add_room(room3)
        assert floor.count_available() == 0

    def test_count_available_mixed(self):
        floor = Floor(1, "First Floor", True)
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, False)
        room3 = Room(103, 1, True)
        room4 = Room(104, 1, False)
        floor.add_room(room1)
        floor.add_room(room2)
        floor.add_room(room3)
        floor.add_room(room4)
        assert floor.count_available() == 2

    def test_count_available_single_room_available(self):
        floor = Floor(1, "First Floor", True)
        room = Room(101, 1, True)
        floor.add_room(room)
        assert floor.count_available() == 1

    def test_count_available_single_room_not_available(self):
        floor = Floor(1, "First Floor", True)
        room = Room(101, 1, False)
        floor.add_room(room)
        assert floor.count_available() == 0

    def test_count_available_after_changing_room_status(self):
        floor = Floor(1, "First Floor", True)
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, True)
        floor.add_room(room1)
        floor.add_room(room2)
        assert floor.count_available() == 2
        room1.is_available = False
        assert floor.count_available() == 1

    def test_add_duplicate_room_object(self):
        floor = Floor(1, "First Floor", True)
        room = Room(101, 1, True)
        floor.add_room(room)
        floor.add_room(room)
        assert len(floor.rooms) == 2  # Same object added twice

    def test_add_rooms_with_same_number(self):
        floor = Floor(1, "First Floor", True)
        room1 = Room(101, 1, True)
        room2 = Room(101, 1, False)  # Different object, same number
        floor.add_room(room1)
        floor.add_room(room2)
        assert len(floor.rooms) == 2

    def test_add_room_maintains_sort_order(self):
        floor = Floor(1, "First Floor", True)
        room1 = Room(101, 1, True)
        room2 = Room(103, 1, True)
        floor.add_room(room1)
        floor.add_room(room2)
        room_middle = Room(102, 1, True)
        floor.add_room(room_middle)
        assert floor.rooms[0].number == 101
        assert floor.rooms[1].number == 102
        assert floor.rooms[2].number == 103

    def test_accessible_boolean_true(self):
        floor = Floor(1, "First", True)
        assert floor.accessible is True

    def test_accessible_boolean_false(self):
        floor = Floor(1, "First", False)
        assert floor.accessible is False
