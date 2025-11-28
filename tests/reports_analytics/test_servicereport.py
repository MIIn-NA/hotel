import pytest
from reports_analytics.ServiceReport import ServiceReport


class TestServiceReport:
    def test_init(self):
        report = ServiceReport("Room Service", 150, "2024-01-01")
        assert report.name == "Room Service"
        assert report.usage == 150
        assert report.date == "2024-01-01"

    def test_init_with_zero_usage(self):
        report = ServiceReport("Laundry", 0, "2024-01-01")
        assert report.usage == 0

    def test_init_with_negative_usage(self):
        report = ServiceReport("Spa", -5, "2024-01-01")
        assert report.usage == -5

    def test_update_usage_positive_count(self):
        report = ServiceReport("Room Service", 100, "2024-01-01")
        report.update_usage(50)
        assert report.usage == 150

    def test_update_usage_zero(self):
        report = ServiceReport("Laundry", 100, "2024-01-01")
        report.update_usage(0)
        assert report.usage == 100

    def test_update_usage_negative_count(self):
        report = ServiceReport("Room Service", 100, "2024-01-01")
        report.update_usage(-50)
        assert report.usage == 100  # Should not change

    def test_update_usage_large_number(self):
        report = ServiceReport("Spa", 50, "2024-01-01")
        report.update_usage(1000)
        assert report.usage == 1050

    def test_update_usage_multiple_times(self):
        report = ServiceReport("Room Service", 100, "2024-01-01")
        report.update_usage(10)
        report.update_usage(20)
        report.update_usage(30)
        assert report.usage == 160

    def test_update_usage_mixed_operations(self):
        report = ServiceReport("Laundry", 100, "2024-01-01")
        report.update_usage(50)
        report.update_usage(-10)  # Should be ignored
        report.update_usage(20)
        assert report.usage == 170

    def test_update_usage_from_zero(self):
        report = ServiceReport("Gym", 0, "2024-01-01")
        report.update_usage(100)
        assert report.usage == 100

    def test_details(self):
        report = ServiceReport("Room Service", 150, "2024-01-01")
        result = report.details()
        assert result == "Room Service used 150 times on 2024-01-01"

    def test_details_with_different_values(self):
        report = ServiceReport("Laundry Service", 75, "2024-02-15")
        result = report.details()
        assert result == "Laundry Service used 75 times on 2024-02-15"

    def test_details_after_update_usage(self):
        report = ServiceReport("Room Service", 100, "2024-01-01")
        report.update_usage(50)
        result = report.details()
        assert result == "Room Service used 150 times on 2024-01-01"

    def test_details_with_zero_usage(self):
        report = ServiceReport("Spa", 0, "2024-01-01")
        result = report.details()
        assert result == "Spa used 0 times on 2024-01-01"

    def test_details_format(self):
        report = ServiceReport("Valet Parking", 200, "2024-03-20")
        result = report.details()
        assert "Valet Parking" in result
        assert "200 times" in result
        assert "2024-03-20" in result

    def test_details_singular_usage(self):
        report = ServiceReport("Concierge", 1, "2024-01-01")
        result = report.details()
        assert result == "Concierge used 1 times on 2024-01-01"

    def test_update_usage_maintains_name_and_date(self):
        report = ServiceReport("Room Service", 100, "2024-01-01")
        report.update_usage(50)
        assert report.name == "Room Service"
        assert report.date == "2024-01-01"

    def test_update_usage_decimal_count(self):
        report = ServiceReport("Gym", 100, "2024-01-01")
        report.update_usage(25)
        assert report.usage == 125

    def test_update_usage_very_large_negative(self):
        report = ServiceReport("Spa", 100, "2024-01-01")
        report.update_usage(-10000)
        assert report.usage == 100  # Should remain unchanged

    def test_multiple_updates_with_negatives(self):
        report = ServiceReport("Room Service", 100, "2024-01-01")
        report.update_usage(50)
        report.update_usage(-25)
        report.update_usage(30)
        assert report.usage == 180  # 100 + 50 + 30 (negative ignored)
