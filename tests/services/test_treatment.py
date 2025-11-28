import pytest
from services.Treatment import Treatment


class TestTreatment:
    def test_init(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        assert treatment.name == "Swedish Massage"
        assert treatment.duration == 60
        assert treatment.price == 100.0

    def test_init_with_different_values(self):
        treatment = Treatment("Hot Stone Therapy", 90, 150.0)
        assert treatment.name == "Hot Stone Therapy"
        assert treatment.duration == 90
        assert treatment.price == 150.0

    def test_init_with_zero_duration(self):
        treatment = Treatment("Quick Treatment", 0, 50.0)
        assert treatment.duration == 0
        assert treatment.price == 50.0

    def test_init_with_zero_price(self):
        treatment = Treatment("Free Treatment", 30, 0.0)
        assert treatment.price == 0.0

    def test_init_with_negative_duration(self):
        treatment = Treatment("Treatment", -30, 100.0)
        assert treatment.duration == -30

    def test_init_with_negative_price(self):
        treatment = Treatment("Treatment", 60, -50.0)
        assert treatment.price == -50.0

    def test_final_price_no_discount(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(0.0)
        assert final == 100.0

    def test_final_price_with_discount(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(20.0)
        assert final == 80.0

    def test_final_price_with_small_discount(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(10.0)
        assert final == 90.0

    def test_final_price_with_large_discount(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(50.0)
        assert final == 50.0

    def test_final_price_discount_equals_price(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(100.0)
        assert final == 0.0

    def test_final_price_discount_exceeds_price(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(150.0)
        assert final == 0.0

    def test_final_price_with_negative_discount(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(-20.0)
        assert final == 100.0

    def test_final_price_negative_discount_returns_original_price(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(-50.0)
        assert final == treatment.price

    def test_final_price_max_function_minimum_zero(self):
        treatment = Treatment("Swedish Massage", 60, 80.0)
        final = treatment.final_price(100.0)
        assert final == 0.0
        assert final >= 0

    def test_final_price_precision(self):
        treatment = Treatment("Swedish Massage", 60, 100.50)
        final = treatment.final_price(20.25)
        assert final == pytest.approx(80.25, rel=1e-9)

    def test_final_price_with_zero_price(self):
        treatment = Treatment("Free Treatment", 30, 0.0)
        final = treatment.final_price(10.0)
        assert final == 0.0

    def test_final_price_zero_price_no_discount(self):
        treatment = Treatment("Free Treatment", 30, 0.0)
        final = treatment.final_price(0.0)
        assert final == 0.0

    def test_final_price_negative_price_with_discount(self):
        treatment = Treatment("Treatment", 60, -50.0)
        final = treatment.final_price(10.0)
        assert final == 0.0

    def test_is_long_exactly_60_minutes(self):
        treatment = Treatment("Standard Treatment", 60, 100.0)
        assert treatment.is_long() is True

    def test_is_long_above_60_minutes(self):
        treatment = Treatment("Extended Treatment", 90, 150.0)
        assert treatment.is_long() is True

    def test_is_long_below_60_minutes(self):
        treatment = Treatment("Quick Treatment", 59, 80.0)
        assert treatment.is_long() is False

    def test_is_long_30_minutes(self):
        treatment = Treatment("Short Treatment", 30, 50.0)
        assert treatment.is_long() is False

    def test_is_long_0_minutes(self):
        treatment = Treatment("Instant Treatment", 0, 0.0)
        assert treatment.is_long() is False

    def test_is_long_negative_duration(self):
        treatment = Treatment("Treatment", -30, 100.0)
        assert treatment.is_long() is False

    def test_is_long_very_long_duration(self):
        treatment = Treatment("All-Day Treatment", 480, 500.0)
        assert treatment.is_long() is True

    def test_is_long_boundary_59(self):
        treatment = Treatment("Treatment", 59, 100.0)
        assert treatment.is_long() is False

    def test_is_long_boundary_60(self):
        treatment = Treatment("Treatment", 60, 100.0)
        assert treatment.is_long() is True

    def test_is_long_boundary_61(self):
        treatment = Treatment("Treatment", 61, 100.0)
        assert treatment.is_long() is True

    def test_empty_string_name(self):
        treatment = Treatment("", 60, 100.0)
        assert treatment.name == ""
        assert treatment.duration == 60
        assert treatment.price == 100.0

    def test_final_price_multiple_calls(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final1 = treatment.final_price(10.0)
        final2 = treatment.final_price(20.0)
        final3 = treatment.final_price(30.0)
        assert final1 == 90.0
        assert final2 == 80.0
        assert final3 == 70.0
        assert treatment.price == 100.0

    def test_final_price_does_not_modify_original_price(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        original_price = treatment.price
        treatment.final_price(50.0)
        assert treatment.price == original_price

    def test_is_long_does_not_modify_duration(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        original_duration = treatment.duration
        treatment.is_long()
        assert treatment.duration == original_duration

    def test_combined_methods(self):
        treatment = Treatment("Deluxe Massage", 90, 200.0)
        assert treatment.is_long() is True
        final = treatment.final_price(50.0)
        assert final == 150.0
        assert treatment.duration == 90
        assert treatment.price == 200.0

    def test_final_price_with_decimal_discount(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(15.50)
        assert final == 84.50

    def test_final_price_very_large_discount(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(10000.0)
        assert final == 0.0

    def test_final_price_very_small_discount(self):
        treatment = Treatment("Swedish Massage", 60, 100.0)
        final = treatment.final_price(0.01)
        assert final == pytest.approx(99.99, rel=1e-9)

    def test_final_price_edge_case_negative_result(self):
        treatment = Treatment("Swedish Massage", 60, 50.0)
        final = treatment.final_price(75.0)
        assert final == 0.0
        assert final >= 0
