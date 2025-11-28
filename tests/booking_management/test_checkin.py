import pytest
from booking_management.CheckIn import CheckIn
from user_management.Guest import Guest


class TestCheckIn:
    def test_init(self):
        checkin = CheckIn("2024-01-15", "14:00", "agent1")
        assert checkin.date == "2024-01-15"
        assert checkin.time == "14:00"
        assert checkin.agent == "agent1"
        assert checkin.guest is None

    def test_assign_guest_valid(self):
        checkin = CheckIn("2024-01-15", "14:00", "agent1")
        guest = Guest("John Doe", "jdoe", False)
        checkin.assign_guest(guest)
        assert checkin.guest == guest
        assert checkin.agent == "agent1-John Doe"

    def test_assign_guest_invalid_type(self):
        checkin = CheckIn("2024-01-15", "14:00", "agent1")
        with pytest.raises(ValueError, match="Expected Guest"):
            checkin.assign_guest("not a guest")

    def test_assign_guest_without_name(self):
        checkin = CheckIn("2024-01-15", "14:00", "agent1")
        guest = Guest("Jane", "jane123", True)
        delattr(guest, "name")
        checkin.assign_guest(guest)
        assert checkin.agent == "agent1"

    def test_summary_without_guest(self):
        checkin = CheckIn("2024-01-15", "14:00", "agent1")
        result = checkin.summary()
        assert result == "2024-01-15 at 14:00"

    def test_summary_with_guest(self):
        checkin = CheckIn("2024-01-15", "14:00", "agent1")
        guest = Guest("Alice Smith", "asmith", True)
        checkin.assign_guest(guest)
        result = checkin.summary()
        assert result == "2024-01-15 at 14:00 checked: Alice Smith"

    def test_summary_format(self):
        checkin = CheckIn("2024-12-25", "09:30", "reception")
        result = checkin.summary()
        assert "at" in result
        assert checkin.date in result
        assert checkin.time in result

    def test_assign_multiple_guests(self):
        checkin = CheckIn("2024-01-15", "14:00", "agent1")
        guest1 = Guest("Bob", "bob1", False)
        guest2 = Guest("Carol", "carol1", False)
        checkin.assign_guest(guest1)
        checkin.assign_guest(guest2)
        assert checkin.agent == "agent1-Bob-Carol"
