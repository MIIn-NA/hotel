import pytest
from reports_analytics.InventoryReport import InventoryReport


class TestInventoryReport:
    def test_init(self):
        report = InventoryReport("Linens", 100, "Q1 2024")
        assert report.category == "Linens"
        assert report.items_count == 100
        assert report.period == "Q1 2024"

    def test_init_with_zero_items(self):
        report = InventoryReport("Towels", 0, "Q2 2024")
        assert report.items_count == 0

    def test_init_with_negative_items(self):
        report = InventoryReport("Supplies", -5, "Q3 2024")
        assert report.items_count == -5

    def test_add_items_positive_number(self):
        report = InventoryReport("Linens", 100, "Q1 2024")
        report.add_items(50)
        assert report.items_count == 150

    def test_add_items_zero(self):
        report = InventoryReport("Towels", 100, "Q1 2024")
        report.add_items(0)
        assert report.items_count == 100

    def test_add_items_negative_number(self):
        report = InventoryReport("Linens", 100, "Q1 2024")
        report.add_items(-50)
        assert report.items_count == 100  # Should not change

    def test_add_items_large_number(self):
        report = InventoryReport("Supplies", 50, "Q1 2024")
        report.add_items(1000)
        assert report.items_count == 1050

    def test_add_items_multiple_times(self):
        report = InventoryReport("Linens", 100, "Q1 2024")
        report.add_items(10)
        report.add_items(20)
        report.add_items(30)
        assert report.items_count == 160

    def test_add_items_mixed_operations(self):
        report = InventoryReport("Towels", 100, "Q1 2024")
        report.add_items(50)
        report.add_items(-10)  # Should be ignored
        report.add_items(20)
        assert report.items_count == 170

    def test_add_items_decimal_number(self):
        report = InventoryReport("Supplies", 100, "Q1 2024")
        report.add_items(25)
        assert report.items_count == 125

    def test_summary(self):
        report = InventoryReport("Linens", 100, "Q1 2024")
        result = report.summary()
        assert result == "Linens: 100 items (Q1 2024)"

    def test_summary_with_different_values(self):
        report = InventoryReport("Towels", 250, "Q2 2024")
        result = report.summary()
        assert result == "Towels: 250 items (Q2 2024)"

    def test_summary_after_add_items(self):
        report = InventoryReport("Supplies", 100, "Q1 2024")
        report.add_items(50)
        result = report.summary()
        assert result == "Supplies: 150 items (Q1 2024)"

    def test_summary_with_zero_items(self):
        report = InventoryReport("Equipment", 0, "Q3 2024")
        result = report.summary()
        assert result == "Equipment: 0 items (Q3 2024)"

    def test_summary_format(self):
        report = InventoryReport("Bed Linens", 500, "January 2024")
        result = report.summary()
        assert "Bed Linens" in result
        assert "500 items" in result
        assert "January 2024" in result

    def test_add_items_from_zero(self):
        report = InventoryReport("Towels", 0, "Q1 2024")
        report.add_items(100)
        assert report.items_count == 100

    def test_add_items_maintains_category_and_period(self):
        report = InventoryReport("Linens", 100, "Q1 2024")
        report.add_items(50)
        assert report.category == "Linens"
        assert report.period == "Q1 2024"

    def test_add_items_very_large_negative(self):
        report = InventoryReport("Supplies", 100, "Q1 2024")
        report.add_items(-10000)
        assert report.items_count == 100  # Should remain unchanged
