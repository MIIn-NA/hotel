import pytest
from services.Event import Event
from services.ConferenceRoom import ConferenceRoom


class TestEvent:
    def test_init(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        assert event.name == "Annual Meeting"
        assert event.date == "2024-12-15"
        assert event.attendees == 100
        assert event.room is None

    def test_init_with_different_values(self):
        event = Event("Workshop", "2024-11-20", 30)
        assert event.name == "Workshop"
        assert event.date == "2024-11-20"
        assert event.attendees == 30

    def test_init_with_zero_attendees(self):
        event = Event("Small Gathering", "2024-10-10", 0)
        assert event.attendees == 0
        assert event.room is None

    def test_assign_room_valid(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        room = ConferenceRoom("CR001", 150, "Main Hall")
        event.assign_room(room)
        assert event.room == room
        assert event.attendees == 100

    def test_assign_room_reduces_attendees_when_capacity_lower(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        room = ConferenceRoom("CR001", 50, "Small Hall")
        event.assign_room(room)
        assert event.room == room
        assert event.attendees == 50

    def test_assign_room_maintains_attendees_when_capacity_equal(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        room = ConferenceRoom("CR001", 100, "Medium Hall")
        event.assign_room(room)
        assert event.room == room
        assert event.attendees == 100

    def test_assign_room_maintains_attendees_when_capacity_higher(self):
        event = Event("Annual Meeting", "2024-12-15", 50)
        room = ConferenceRoom("CR001", 100, "Large Hall")
        event.assign_room(room)
        assert event.room == room
        assert event.attendees == 50

    def test_assign_room_invalid_type(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        with pytest.raises(ValueError, match="Invalid conference room."):
            event.assign_room("not a room")

    def test_assign_room_none(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        with pytest.raises(ValueError, match="Invalid conference room."):
            event.assign_room(None)

    def test_assign_room_invalid_object(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        with pytest.raises(ValueError, match="Invalid conference room."):
            event.assign_room({"code": "CR001"})

    def test_assign_room_with_zero_capacity(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        room = ConferenceRoom("CR001", 0, "Closed Room")
        event.assign_room(room)
        assert event.attendees == 0

    def test_assign_room_multiple_times(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        room1 = ConferenceRoom("CR001", 50, "Small Hall")
        room2 = ConferenceRoom("CR002", 200, "Large Hall")
        event.assign_room(room1)
        assert event.attendees == 50
        event.assign_room(room2)
        assert event.room == room2
        assert event.attendees == 50

    def test_summary_without_room(self):
        event = Event("Team Workshop", "2024-12-15", 100)
        summary = event.summary()
        assert summary == "Team Workshop on 2024-12-15"
        assert " in " not in summary

    def test_summary_with_room(self):
        event = Event("Annual Meeting", "2024-12-15", 100)
        room = ConferenceRoom("CR001", 150, "Main Hall")
        event.assign_room(room)
        summary = event.summary()
        assert summary == "Annual Meeting on 2024-12-15 in Main Hall"

    def test_summary_with_room_different_label(self):
        event = Event("Workshop", "2024-11-20", 30)
        room = ConferenceRoom("CR002", 50, "Executive Boardroom")
        event.assign_room(room)
        summary = event.summary()
        assert summary == "Workshop on 2024-11-20 in Executive Boardroom"

    def test_summary_format(self):
        event = Event("Team Building", "2024-10-05", 25)
        summary = event.summary()
        assert event.name in summary
        assert event.date in summary
        assert "on" in summary

    def test_empty_string_parameters(self):
        event = Event("", "", 10)
        assert event.name == ""
        assert event.date == ""
        assert event.attendees == 10

    def test_negative_attendees(self):
        event = Event("Event", "2024-12-15", -10)
        assert event.attendees == -10
        room = ConferenceRoom("CR001", 50, "Hall")
        event.assign_room(room)
        assert event.attendees == -10

    def test_assign_room_to_zero_attendees_event(self):
        event = Event("Private Event", "2024-12-15", 0)
        room = ConferenceRoom("CR001", 50, "Hall")
        event.assign_room(room)
        assert event.attendees == 0
        assert event.room == room

    def test_assign_room_with_negative_capacity(self):
        event = Event("Event", "2024-12-15", 100)
        room = ConferenceRoom("CR001", -10, "Unusual Room")
        event.assign_room(room)
        assert event.attendees == -10
