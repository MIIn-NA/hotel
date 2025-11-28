import pytest
from booking_management.Discount import Discount


class TestDiscount:
    def test_init(self):
        discount = Discount("SAVE10", 10.0, "10 dollars off")
        assert discount.code == "SAVE10"
        assert discount.amount == 10.0
        assert discount.description == "10 dollars off"

    def test_apply_basic(self):
        discount = Discount("SAVE10", 10.0, "10 dollars off")
        result = discount.apply(100.0)
        assert result == 90.0

    def test_apply_exact_amount(self):
        discount = Discount("SAVE50", 50.0, "50 off")
        result = discount.apply(50.0)
        assert result == 0.0

    def test_apply_more_than_total(self):
        discount = Discount("SAVE100", 100.0, "100 off")
        result = discount.apply(50.0)
        assert result == 0.0

    def test_apply_negative_discount(self):
        discount = Discount("BAD", -10.0, "invalid")
        result = discount.apply(100.0)
        assert result == 100.0

    def test_apply_zero_discount(self):
        discount = Discount("ZERO", 0.0, "no discount")
        result = discount.apply(100.0)
        assert result == 100.0

    def test_is_valid_true(self):
        discount = Discount("SAVE10", 10.0, "valid discount")
        assert discount.is_valid() is True

    def test_is_valid_short_code(self):
        discount = Discount("AB", 10.0, "too short")
        assert discount.is_valid() is False

    def test_is_valid_negative_amount(self):
        discount = Discount("CODE", -5.0, "negative amount")
        assert discount.is_valid() is False

    def test_is_valid_exact_min_code_length(self):
        discount = Discount("ABC", 10.0, "minimum code")
        assert discount.is_valid() is True

    def test_is_valid_zero_amount(self):
        discount = Discount("CODE", 0.0, "zero amount")
        assert discount.is_valid() is True

    def test_apply_to_zero_total(self):
        discount = Discount("SAVE10", 10.0, "10 off")
        result = discount.apply(0.0)
        assert result == 0.0
