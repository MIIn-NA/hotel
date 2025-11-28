import pytest
from reports_analytics.Analytics import Analytics


class TestAnalytics:
    def test_init(self):
        analytics = Analytics("revenue", 1000.0, "USD")
        assert analytics.metric == "revenue"
        assert analytics.value == 1000.0
        assert analytics.label == "USD"

    def test_init_with_zero_value(self):
        analytics = Analytics("profit", 0.0, "EUR")
        assert analytics.value == 0.0
        assert analytics.metric == "profit"

    def test_init_with_negative_value(self):
        analytics = Analytics("loss", -500.0, "GBP")
        assert analytics.value == -500.0

    def test_upscale_positive_factor(self):
        analytics = Analytics("sales", 100.0, "USD")
        analytics.upscale(2.0)
        assert analytics.value == 200.0

    def test_upscale_decimal_factor(self):
        analytics = Analytics("revenue", 100.0, "USD")
        analytics.upscale(1.5)
        assert analytics.value == 150.0

    def test_upscale_zero_factor(self):
        analytics = Analytics("sales", 100.0, "USD")
        analytics.upscale(0.0)
        assert analytics.value == 10.0  # min factor is 0.1

    def test_upscale_negative_factor(self):
        analytics = Analytics("revenue", 100.0, "USD")
        analytics.upscale(-1.0)
        assert analytics.value == 10.0  # min factor is 0.1

    def test_upscale_small_positive_factor(self):
        analytics = Analytics("metric", 100.0, "USD")
        analytics.upscale(0.05)
        assert analytics.value == 10.0  # min factor is 0.1

    def test_upscale_large_factor(self):
        analytics = Analytics("growth", 10.0, "USD")
        analytics.upscale(100.0)
        assert analytics.value == 1000.0

    def test_upscale_multiple_times(self):
        analytics = Analytics("value", 10.0, "USD")
        analytics.upscale(2.0)
        analytics.upscale(3.0)
        assert analytics.value == 60.0

    def test_describe(self):
        analytics = Analytics("revenue", 1000.0, "USD")
        result = analytics.describe()
        assert result == "revenue = 1000.0 (USD)"

    def test_describe_with_different_values(self):
        analytics = Analytics("profit", 250.5, "EUR")
        result = analytics.describe()
        assert result == "profit = 250.5 (EUR)"

    def test_describe_after_upscale(self):
        analytics = Analytics("sales", 100.0, "USD")
        analytics.upscale(2.0)
        result = analytics.describe()
        assert result == "sales = 200.0 (USD)"

    def test_describe_with_negative_value(self):
        analytics = Analytics("loss", -100.0, "GBP")
        result = analytics.describe()
        assert result == "loss = -100.0 (GBP)"

    def test_describe_with_zero_value(self):
        analytics = Analytics("neutral", 0.0, "USD")
        result = analytics.describe()
        assert result == "neutral = 0.0 (USD)"
