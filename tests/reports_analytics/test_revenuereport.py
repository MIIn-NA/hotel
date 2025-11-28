import pytest
from reports_analytics.RevenueReport import RevenueReport


class TestRevenueReport:
    def test_init(self):
        report = RevenueReport("Room Sales", 50000.0, "Q1 2024")
        assert report.category == "Room Sales"
        assert report.revenue == 50000.0
        assert report.period == "Q1 2024"

    def test_init_with_zero_revenue(self):
        report = RevenueReport("Services", 0.0, "Q2 2024")
        assert report.revenue == 0.0

    def test_init_with_negative_revenue(self):
        report = RevenueReport("Refunds", -1000.0, "Q3 2024")
        assert report.revenue == -1000.0

    def test_adjust_positive_amount(self):
        report = RevenueReport("Room Sales", 1000.0, "Q1 2024")
        report.adjust(500.0)
        assert report.revenue == 1500.0

    def test_adjust_negative_amount(self):
        report = RevenueReport("Room Sales", 1000.0, "Q1 2024")
        report.adjust(-200.0)
        assert report.revenue == 800.0

    def test_adjust_zero_amount(self):
        report = RevenueReport("Room Sales", 1000.0, "Q1 2024")
        report.adjust(0.0)
        assert report.revenue == 1000.0

    def test_adjust_large_negative_sets_to_zero(self):
        report = RevenueReport("Room Sales", 500.0, "Q1 2024")
        report.adjust(-1000.0)
        assert report.revenue == 0.0

    def test_adjust_prevents_negative_revenue(self):
        report = RevenueReport("Services", 100.0, "Q1 2024")
        report.adjust(-200.0)
        assert report.revenue == 0.0

    def test_adjust_multiple_times(self):
        report = RevenueReport("Room Sales", 1000.0, "Q1 2024")
        report.adjust(100.0)
        report.adjust(200.0)
        report.adjust(-50.0)
        assert report.revenue == 1250.0

    def test_adjust_decimal_amount(self):
        report = RevenueReport("Services", 1000.0, "Q1 2024")
        report.adjust(123.45)
        assert report.revenue == 1123.45

    def test_adjust_from_zero(self):
        report = RevenueReport("Room Sales", 0.0, "Q1 2024")
        report.adjust(100.0)
        assert report.revenue == 100.0

    def test_adjust_to_zero(self):
        report = RevenueReport("Services", 100.0, "Q1 2024")
        report.adjust(-100.0)
        assert report.revenue == 0.0

    def test_adjust_exactly_to_zero(self):
        report = RevenueReport("Room Sales", 500.0, "Q1 2024")
        report.adjust(-500.0)
        assert report.revenue == 0.0

    def test_detail(self):
        report = RevenueReport("Room Sales", 50000.0, "Q1 2024")
        result = report.detail()
        assert result == "Room Sales: 50000.0 (Q1 2024)"

    def test_detail_with_different_values(self):
        report = RevenueReport("Food & Beverage", 25000.5, "Q2 2024")
        result = report.detail()
        assert result == "Food & Beverage: 25000.5 (Q2 2024)"

    def test_detail_after_adjust(self):
        report = RevenueReport("Room Sales", 1000.0, "Q1 2024")
        report.adjust(500.0)
        result = report.detail()
        assert result == "Room Sales: 1500.0 (Q1 2024)"

    def test_detail_with_zero_revenue(self):
        report = RevenueReport("Services", 0.0, "Q3 2024")
        result = report.detail()
        assert result == "Services: 0.0 (Q3 2024)"

    def test_detail_format(self):
        report = RevenueReport("Conference Rooms", 12345.67, "January 2024")
        result = report.detail()
        assert "Conference Rooms" in result
        assert "12345.67" in result
        assert "January 2024" in result

    def test_multiple_adjustments_and_detail(self):
        report = RevenueReport("Room Sales", 1000.0, "Q1 2024")
        report.adjust(100.0)
        report.adjust(-50.0)
        result = report.detail()
        assert result == "Room Sales: 1050.0 (Q1 2024)"

    def test_adjust_preserves_category_and_period(self):
        report = RevenueReport("Room Sales", 1000.0, "Q1 2024")
        report.adjust(500.0)
        assert report.category == "Room Sales"
        assert report.period == "Q1 2024"

    def test_adjust_with_large_positive(self):
        report = RevenueReport("Services", 100.0, "Q1 2024")
        report.adjust(10000.0)
        assert report.revenue == 10100.0

    def test_adjust_boundary_negative(self):
        report = RevenueReport("Room Sales", 0.01, "Q1 2024")
        report.adjust(-0.02)
        assert report.revenue == 0.0
