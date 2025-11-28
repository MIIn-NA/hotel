import pytest
from booking_management.RatePlan import RatePlan


class TestRatePlan:
    def test_init(self):
        plan = RatePlan("Standard", 100.0, "flexible")
        assert plan.name == "Standard"
        assert plan.price == 100.0
        assert plan.policy == "flexible"

    def test_calculate_basic(self):
        plan = RatePlan("Standard", 100.0, "flexible")
        result = plan.calculate(3)
        assert result == 300.0

    def test_calculate_nonrefundable_discount(self):
        plan = RatePlan("Saver", 100.0, "nonrefundable")
        result = plan.calculate(2)
        assert result == 180.0

    def test_calculate_nonrefundable_case_insensitive(self):
        plan = RatePlan("Saver", 100.0, "NONREFUNDABLE")
        result = plan.calculate(1)
        assert result == 90.0

    def test_calculate_one_night(self):
        plan = RatePlan("Standard", 150.0, "flexible")
        result = plan.calculate(1)
        assert result == 150.0

    def test_calculate_zero_nights(self):
        plan = RatePlan("Standard", 100.0, "flexible")
        result = plan.calculate(0)
        assert result == 0.0

    def test_calculate_rounding(self):
        plan = RatePlan("Premium", 99.99, "flexible")
        result = plan.calculate(3)
        assert result == 299.97

    def test_is_flexible_true(self):
        plan = RatePlan("Standard", 100.0, "flexible")
        assert plan.is_flexible() is True

    def test_is_flexible_false(self):
        plan = RatePlan("Saver", 100.0, "nonrefundable")
        assert plan.is_flexible() is False

    def test_is_flexible_case_insensitive(self):
        plan = RatePlan("Standard", 100.0, "FLEXIBLE")
        assert plan.is_flexible() is True

    def test_is_flexible_partial_match(self):
        plan = RatePlan("Standard", 100.0, "superflex")
        assert plan.is_flexible() is True

    def test_calculate_nonrefundable_with_flex_in_policy(self):
        plan = RatePlan("Mixed", 100.0, "nonrefundable-flex")
        result = plan.calculate(2)
        assert result == 180.0
