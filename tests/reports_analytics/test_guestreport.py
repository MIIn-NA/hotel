import pytest
from reports_analytics.GuestReport import GuestReport
from user_management.Guest import Guest


class TestGuestReport:
    def test_init(self):
        report = GuestReport("Q1 2024", 5, 20)
        assert report.period == "Q1 2024"
        assert report.vip_count == 5
        assert report.total_count == 20
        assert report.guests == []

    def test_init_with_zero_counts(self):
        report = GuestReport("Q2 2024", 0, 0)
        assert report.vip_count == 0
        assert report.total_count == 0

    def test_init_guests_list_empty(self):
        report = GuestReport("Q1 2024", 5, 20)
        assert isinstance(report.guests, list)
        assert len(report.guests) == 0

    def test_add_guest_valid(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest = Guest("John Doe", "G001", False)
        report.add_guest(guest)
        assert len(report.guests) == 1
        assert report.guests[0] == guest

    def test_add_guest_increases_total_count(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest = Guest("Jane Smith", "G002", False)
        report.add_guest(guest)
        assert report.total_count == 1

    def test_add_guest_vip_increases_vip_count(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest = Guest("Bob Johnson", "G003", True)
        report.add_guest(guest)
        assert report.vip_count == 1
        assert report.total_count == 1

    def test_add_guest_non_vip_no_vip_increase(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest = Guest("Alice Brown", "G004", False)
        report.add_guest(guest)
        assert report.vip_count == 0
        assert report.total_count == 1

    def test_add_guest_invalid_type(self):
        report = GuestReport("Q1 2024", 0, 0)
        with pytest.raises(ValueError, match="Invalid Guest"):
            report.add_guest("not a guest")

    def test_add_guest_invalid_type_dict(self):
        report = GuestReport("Q1 2024", 0, 0)
        with pytest.raises(ValueError, match="Invalid Guest"):
            report.add_guest({"name": "Test"})

    def test_add_guest_invalid_type_none(self):
        report = GuestReport("Q1 2024", 0, 0)
        with pytest.raises(ValueError, match="Invalid Guest"):
            report.add_guest(None)

    def test_add_multiple_guests(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest1 = Guest("John Doe", "G001", True)
        guest2 = Guest("Jane Smith", "G002", False)
        guest3 = Guest("Bob Johnson", "G003", True)
        report.add_guest(guest1)
        report.add_guest(guest2)
        report.add_guest(guest3)
        assert len(report.guests) == 3
        assert report.total_count == 3
        assert report.vip_count == 2

    def test_vip_ratio_with_zero_total(self):
        report = GuestReport("Q1 2024", 0, 0)
        assert report.vip_ratio() == 0.0

    def test_vip_ratio_all_vip(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest1 = Guest("John Doe", "G001", True)
        guest2 = Guest("Jane Smith", "G002", True)
        report.add_guest(guest1)
        report.add_guest(guest2)
        assert report.vip_ratio() == 1.0

    def test_vip_ratio_half_vip(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest1 = Guest("John Doe", "G001", True)
        guest2 = Guest("Jane Smith", "G002", False)
        report.add_guest(guest1)
        report.add_guest(guest2)
        assert report.vip_ratio() == 0.5

    def test_vip_ratio_none_vip(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest1 = Guest("John Doe", "G001", False)
        guest2 = Guest("Jane Smith", "G002", False)
        report.add_guest(guest1)
        report.add_guest(guest2)
        assert report.vip_ratio() == 0.0

    def test_vip_ratio_rounding(self):
        report = GuestReport("Q1 2024", 0, 0)
        guest1 = Guest("John Doe", "G001", True)
        guest2 = Guest("Jane Smith", "G002", False)
        guest3 = Guest("Bob Johnson", "G003", False)
        report.add_guest(guest1)
        report.add_guest(guest2)
        report.add_guest(guest3)
        assert report.vip_ratio() == 0.333

    def test_vip_ratio_with_initial_values(self):
        report = GuestReport("Q1 2024", 10, 50)
        assert report.vip_ratio() == 0.2

    def test_vip_ratio_precision(self):
        report = GuestReport("Q1 2024", 0, 0)
        for i in range(7):
            guest = Guest(f"Guest {i}", f"G{i:03d}", i < 2)
            report.add_guest(guest)
        # 2 VIP out of 7 total = 0.285714... rounded to 3 decimals = 0.286
        assert report.vip_ratio() == 0.286

    def test_add_guest_updates_ratio(self):
        report = GuestReport("Q1 2024", 0, 0)
        assert report.vip_ratio() == 0.0
        guest = Guest("John Doe", "G001", True)
        report.add_guest(guest)
        assert report.vip_ratio() == 1.0
        guest2 = Guest("Jane Smith", "G002", False)
        report.add_guest(guest2)
        assert report.vip_ratio() == 0.5
