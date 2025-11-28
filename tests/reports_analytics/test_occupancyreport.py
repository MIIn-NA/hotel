import pytest
from reports_analytics.OccupancyReport import OccupancyReport
from hotel_entities.Room import Room


class TestOccupancyReport:
    def test_init(self):
        report = OccupancyReport("2024-01-01", 100, 75)
        assert report.date == "2024-01-01"
        assert report.total_rooms == 100
        assert report.occupied == 75
        assert report.rooms == []

    def test_init_with_zero_counts(self):
        report = OccupancyReport("2024-01-01", 0, 0)
        assert report.total_rooms == 0
        assert report.occupied == 0

    def test_init_rooms_list_empty(self):
        report = OccupancyReport("2024-01-01", 100, 50)
        assert isinstance(report.rooms, list)
        assert len(report.rooms) == 0

    def test_register_room_valid(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        room = Room(101, 1, True)
        report.register_room(room)
        assert len(report.rooms) == 1
        assert report.rooms[0] == room

    def test_register_room_available_no_occupied_increase(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        room = Room(101, 1, True)
        report.register_room(room)
        assert report.occupied == 0

    def test_register_room_not_available_increases_occupied(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        room = Room(102, 1, False)
        report.register_room(room)
        assert report.occupied == 1

    def test_register_room_invalid_type(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        with pytest.raises(ValueError, match="Invalid Room"):
            report.register_room("not a room")

    def test_register_room_invalid_type_dict(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        with pytest.raises(ValueError, match="Invalid Room"):
            report.register_room({"number": 101})

    def test_register_room_invalid_type_none(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        with pytest.raises(ValueError, match="Invalid Room"):
            report.register_room(None)

    def test_register_multiple_rooms(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        room1 = Room(101, 1, True)
        room2 = Room(102, 1, False)
        room3 = Room(103, 2, False)
        report.register_room(room1)
        report.register_room(room2)
        report.register_room(room3)
        assert len(report.rooms) == 3
        assert report.occupied == 2

    def test_occupancy_rate_with_zero_total(self):
        report = OccupancyReport("2024-01-01", 0, 0)
        assert report.occupancy_rate() == 0.0

    def test_occupancy_rate_fully_occupied(self):
        report = OccupancyReport("2024-01-01", 100, 100)
        assert report.occupancy_rate() == 100.0

    def test_occupancy_rate_half_occupied(self):
        report = OccupancyReport("2024-01-01", 100, 50)
        assert report.occupancy_rate() == 50.0

    def test_occupancy_rate_zero_occupied(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        assert report.occupancy_rate() == 0.0

    def test_occupancy_rate_with_rooms(self):
        report = OccupancyReport("2024-01-01", 10, 0)
        room1 = Room(101, 1, False)
        room2 = Room(102, 1, False)
        room3 = Room(103, 2, True)
        report.register_room(room1)
        report.register_room(room2)
        report.register_room(room3)
        assert report.occupancy_rate() == 20.0  # 2 out of 10

    def test_occupancy_rate_rounding(self):
        report = OccupancyReport("2024-01-01", 3, 1)
        assert report.occupancy_rate() == 33.33

    def test_occupancy_rate_precision(self):
        report = OccupancyReport("2024-01-01", 7, 2)
        # 2/7 * 100 = 28.571428... rounded to 2 decimals = 28.57
        assert report.occupancy_rate() == 28.57

    def test_occupancy_rate_after_registering_rooms(self):
        report = OccupancyReport("2024-01-01", 5, 0)
        assert report.occupancy_rate() == 0.0
        room = Room(101, 1, False)
        report.register_room(room)
        assert report.occupancy_rate() == 20.0

    def test_register_room_maintains_date(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        room = Room(101, 1, True)
        report.register_room(room)
        assert report.date == "2024-01-01"

    def test_multiple_available_rooms(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        for i in range(5):
            room = Room(101 + i, 1, True)
            report.register_room(room)
        assert len(report.rooms) == 5
        assert report.occupied == 0

    def test_multiple_occupied_rooms(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        for i in range(5):
            room = Room(101 + i, 1, False)
            report.register_room(room)
        assert len(report.rooms) == 5
        assert report.occupied == 5

    def test_mixed_room_availability(self):
        report = OccupancyReport("2024-01-01", 100, 0)
        for i in range(10):
            room = Room(101 + i, 1, i % 2 == 0)  # Every other room is available
            report.register_room(room)
        assert len(report.rooms) == 10
        assert report.occupied == 5  # Half are not available
