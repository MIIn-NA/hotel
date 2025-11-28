import pytest
from reports_analytics.DashBoard import Dashboard


class TestDashboard:
    def test_init(self):
        dashboard = Dashboard("Sales Dashboard", "dark", "1.0")
        assert dashboard.title == "Sales Dashboard"
        assert dashboard.theme == "dark"
        assert dashboard.version == "1.0"

    def test_init_with_light_theme(self):
        dashboard = Dashboard("Analytics", "light", "2.0")
        assert dashboard.theme == "light"

    def test_init_with_empty_title(self):
        dashboard = Dashboard("", "dark", "1.0")
        assert dashboard.title == ""

    def test_switch_theme(self):
        dashboard = Dashboard("Dashboard", "light", "1.0")
        dashboard.switch_theme("dark")
        assert dashboard.theme == "dark"

    def test_switch_theme_with_spaces(self):
        dashboard = Dashboard("Dashboard", "light", "1.0")
        dashboard.switch_theme("  DARK  ")
        assert dashboard.theme == "dark"

    def test_switch_theme_uppercase(self):
        dashboard = Dashboard("Dashboard", "dark", "1.0")
        dashboard.switch_theme("LIGHT")
        assert dashboard.theme == "light"

    def test_switch_theme_mixed_case(self):
        dashboard = Dashboard("Dashboard", "dark", "1.0")
        dashboard.switch_theme("LiGhT")
        assert dashboard.theme == "light"

    def test_switch_theme_multiple_times(self):
        dashboard = Dashboard("Dashboard", "light", "1.0")
        dashboard.switch_theme("dark")
        dashboard.switch_theme("light")
        dashboard.switch_theme("dark")
        assert dashboard.theme == "dark"

    def test_switch_theme_with_custom_theme(self):
        dashboard = Dashboard("Dashboard", "light", "1.0")
        dashboard.switch_theme("custom")
        assert dashboard.theme == "custom"

    def test_info(self):
        dashboard = Dashboard("Sales Dashboard", "dark", "1.0")
        result = dashboard.info()
        assert result == "Sales Dashboard [dark] v1.0"

    def test_info_with_different_values(self):
        dashboard = Dashboard("Analytics Board", "light", "2.5")
        result = dashboard.info()
        assert result == "Analytics Board [light] v2.5"

    def test_info_after_theme_switch(self):
        dashboard = Dashboard("Dashboard", "light", "1.0")
        dashboard.switch_theme("dark")
        result = dashboard.info()
        assert result == "Dashboard [dark] v1.0"

    def test_info_with_empty_title(self):
        dashboard = Dashboard("", "dark", "1.0")
        result = dashboard.info()
        assert result == " [dark] v1.0"

    def test_info_with_special_characters(self):
        dashboard = Dashboard("Dashboard 2.0", "dark", "1.0.1")
        result = dashboard.info()
        assert result == "Dashboard 2.0 [dark] v1.0.1"

    def test_theme_persistence(self):
        dashboard = Dashboard("Test", "light", "1.0")
        original_theme = dashboard.theme
        dashboard.switch_theme("dark")
        assert dashboard.theme != original_theme
        assert dashboard.theme == "dark"
