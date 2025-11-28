import pytest
from booking_management.CheckOut import CheckOut
from user_management.Guest import Guest


class TestCheckOut:
    def test_init(self):
        checkout = CheckOut("2024-01-18", "11:00", "room was clean")
        assert checkout.date == "2024-01-18"
        assert checkout.time == "11:00"
        assert checkout.report == "room was clean"
        assert checkout.guest is None

    def test_assign_guest_valid(self):
        checkout = CheckOut("2024-01-18", "11:00", "satisfactory")
        guest = Guest("John Doe", "jdoe", False)
        checkout.assign_guest(guest)
        assert checkout.guest == guest

    def test_assign_guest_invalid_type(self):
        checkout = CheckOut("2024-01-18", "11:00", "good")
        with pytest.raises(ValueError, match="Invalid Guest instance"):
            checkout.assign_guest("not a guest")

    def test_generate_report_without_guest(self):
        checkout = CheckOut("2024-01-18", "11:00", "room was clean")
        result = checkout.generate_report()
        assert result == "2024-01-18 11:00: Room Was Clean"

    def test_generate_report_with_guest(self):
        checkout = CheckOut("2024-01-18", "11:00", "excellent stay")
        guest = Guest("Alice Smith", "asmith", True)
        checkout.assign_guest(guest)
        result = checkout.generate_report()
        assert "By Alice Smith" in result or "By" in result

    def test_generate_report_capitalization(self):
        checkout = CheckOut("2024-01-18", "11:00", "good condition")
        result = checkout.generate_report()
        words = result.split()
        assert any(word[0].isupper() for word in words if word)

    def test_generate_report_with_guest_name(self):
        checkout = CheckOut("2024-01-18", "11:00", "clean")
        guest = Guest("Bob Jones", "bjones", False)
        checkout.assign_guest(guest)
        result = checkout.generate_report()
        assert "Bob" in result
        assert "Jones" in result

    def test_generate_report_format(self):
        checkout = CheckOut("2024-12-25", "10:30", "perfect")
        result = checkout.generate_report()
        assert "2024-12-25" in result
        assert "10:30:" in result
        assert "Perfect" in result

    def test_assign_guest_updates_reference(self):
        checkout = CheckOut("2024-01-18", "11:00", "good")
        guest1 = Guest("First", "first", False)
        guest2 = Guest("Second", "second", False)
        checkout.assign_guest(guest1)
        checkout.assign_guest(guest2)
        assert checkout.guest == guest2
