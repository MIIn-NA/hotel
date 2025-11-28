import pytest
from reports_analytics.Forecast import Forecast


class TestForecast:
    def test_init(self):
        forecast = Forecast("Q1 2024", 50000.0, "Revenue")
        assert forecast.period == "Q1 2024"
        assert forecast.expected == 50000.0
        assert forecast.label == "Revenue"

    def test_init_with_zero_expected(self):
        forecast = Forecast("Q2 2024", 0.0, "Sales")
        assert forecast.expected == 0.0

    def test_init_with_negative_expected(self):
        forecast = Forecast("Q3 2024", -1000.0, "Loss")
        assert forecast.expected == -1000.0

    def test_adjust_positive_delta(self):
        forecast = Forecast("Q1 2024", 1000.0, "Revenue")
        forecast.adjust(500.0)
        assert forecast.expected == 1500.0

    def test_adjust_negative_delta(self):
        forecast = Forecast("Q1 2024", 1000.0, "Revenue")
        forecast.adjust(-200.0)
        assert forecast.expected == 800.0

    def test_adjust_zero_delta(self):
        forecast = Forecast("Q1 2024", 1000.0, "Revenue")
        forecast.adjust(0.0)
        assert forecast.expected == 1000.0

    def test_adjust_large_negative_delta(self):
        forecast = Forecast("Q1 2024", 500.0, "Revenue")
        forecast.adjust(-1000.0)
        assert forecast.expected == 0.0  # max(0, 500 - 1000)

    def test_adjust_prevents_negative(self):
        forecast = Forecast("Q1 2024", 100.0, "Revenue")
        forecast.adjust(-200.0)
        assert forecast.expected == 0.0

    def test_adjust_multiple_times(self):
        forecast = Forecast("Q1 2024", 1000.0, "Revenue")
        forecast.adjust(100.0)
        forecast.adjust(200.0)
        forecast.adjust(-50.0)
        assert forecast.expected == 1250.0

    def test_adjust_decimal_delta(self):
        forecast = Forecast("Q1 2024", 1000.0, "Revenue")
        forecast.adjust(123.45)
        assert forecast.expected == 1123.45

    def test_adjust_from_zero(self):
        forecast = Forecast("Q1 2024", 0.0, "Revenue")
        forecast.adjust(100.0)
        assert forecast.expected == 100.0

    def test_adjust_to_zero(self):
        forecast = Forecast("Q1 2024", 100.0, "Revenue")
        forecast.adjust(-100.0)
        assert forecast.expected == 0.0

    def test_output(self):
        forecast = Forecast("Q1 2024", 50000.0, "Revenue")
        result = forecast.output()
        assert result == "Q1 2024: 50000.0 (Revenue)"

    def test_output_with_different_values(self):
        forecast = Forecast("Q2 2024", 75000.5, "Sales")
        result = forecast.output()
        assert result == "Q2 2024: 75000.5 (Sales)"

    def test_output_after_adjust(self):
        forecast = Forecast("Q1 2024", 1000.0, "Revenue")
        forecast.adjust(500.0)
        result = forecast.output()
        assert result == "Q1 2024: 1500.0 (Revenue)"

    def test_output_with_zero_expected(self):
        forecast = Forecast("Q3 2024", 0.0, "Profit")
        result = forecast.output()
        assert result == "Q3 2024: 0.0 (Profit)"

    def test_output_format(self):
        forecast = Forecast("January 2024", 12345.67, "Monthly Revenue")
        result = forecast.output()
        assert "January 2024" in result
        assert "12345.67" in result
        assert "Monthly Revenue" in result

    def test_multiple_adjustments_and_output(self):
        forecast = Forecast("Q1 2024", 1000.0, "Revenue")
        forecast.adjust(100.0)
        forecast.adjust(-50.0)
        result = forecast.output()
        assert result == "Q1 2024: 1050.0 (Revenue)"

    def test_adjust_preserves_period_and_label(self):
        forecast = Forecast("Q1 2024", 1000.0, "Revenue")
        forecast.adjust(500.0)
        assert forecast.period == "Q1 2024"
        assert forecast.label == "Revenue"
