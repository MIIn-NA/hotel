import pytest
from hotel_entities.RoomType import RoomType


class TestRoomType:
    def test_init(self):
        room_type = RoomType("Deluxe", 2, 150.0)
        assert room_type.name == "Deluxe"
        assert room_type.capacity == 2
        assert room_type.base_price == 150.0

    def test_init_with_zero_capacity(self):
        room_type = RoomType("Studio", 0, 80.0)
        assert room_type.capacity == 0

    def test_init_with_negative_capacity(self):
        room_type = RoomType("Virtual", -1, 50.0)
        assert room_type.capacity == -1

    def test_init_with_zero_price(self):
        room_type = RoomType("Free", 1, 0.0)
        assert room_type.base_price == 0.0

    def test_init_with_negative_price(self):
        room_type = RoomType("Discount", 2, -10.0)
        assert room_type.base_price == -10.0

    def test_init_with_empty_name(self):
        room_type = RoomType("", 2, 100.0)
        assert room_type.name == ""

    def test_calculate_price_zero_nights(self):
        room_type = RoomType("Standard", 2, 100.0)
        price = room_type.calculate_price(0)
        assert price == 100.0

    def test_calculate_price_one_night(self):
        room_type = RoomType("Standard", 2, 100.0)
        price = room_type.calculate_price(1)
        # base_price + (base_price * 0.1) = 100 + 10 = 110
        assert price == 110.0

    def test_calculate_price_two_nights(self):
        room_type = RoomType("Standard", 2, 100.0)
        price = room_type.calculate_price(2)
        # base_price + (base_price * 0.1 * 2) = 100 + 20 = 120
        assert price == 120.0

    def test_calculate_price_three_nights(self):
        room_type = RoomType("Standard", 2, 100.0)
        price = room_type.calculate_price(3)
        # base_price + (base_price * 0.1 * 3) = 100 + 30 = 130
        assert price == 130.0

    def test_calculate_price_multiple_nights(self):
        room_type = RoomType("Deluxe", 2, 200.0)
        price = room_type.calculate_price(5)
        # base_price + (base_price * 0.1 * 5) = 200 + 100 = 300
        assert price == 300.0

    def test_calculate_price_rounding(self):
        room_type = RoomType("Economy", 2, 99.99)
        price = room_type.calculate_price(1)
        # base_price + (base_price * 0.1) = 99.99 + 9.999 = 109.989
        # Rounded to 2 decimals = 109.99
        assert price == 109.99

    def test_calculate_price_rounding_multiple_nights(self):
        room_type = RoomType("Budget", 2, 33.33)
        price = room_type.calculate_price(3)
        # base_price + (base_price * 0.1 * 3) = 33.33 + 9.999 = 43.329
        # Rounded to 2 decimals = 43.33
        assert price == 43.33

    def test_calculate_price_negative_nights(self):
        room_type = RoomType("Standard", 2, 100.0)
        price = room_type.calculate_price(-1)
        # Loop runs -1 times (doesn't execute), so just base_price
        assert price == 100.0

    def test_calculate_price_large_number_of_nights(self):
        room_type = RoomType("Suite", 4, 300.0)
        price = room_type.calculate_price(30)
        # base_price + (base_price * 0.1 * 30) = 300 + 900 = 1200
        assert price == 1200.0

    def test_calculate_price_with_zero_base_price(self):
        room_type = RoomType("Free", 1, 0.0)
        price = room_type.calculate_price(5)
        # 0 + (0 * 0.1 * 5) = 0
        assert price == 0.0

    def test_calculate_price_with_negative_base_price(self):
        room_type = RoomType("Discount", 2, -100.0)
        price = room_type.calculate_price(2)
        # -100 + (-100 * 0.1 * 2) = -100 + (-20) = -120
        assert price == -120.0

    def test_is_large_true(self):
        room_type = RoomType("Family Suite", 4, 100.0)
        assert room_type.is_large() is True

    def test_is_large_false_small_capacity(self):
        room_type = RoomType("Single", 1, 100.0)
        assert room_type.is_large() is False

    def test_is_large_false_low_price(self):
        room_type = RoomType("Quad", 4, 50.0)
        assert room_type.is_large() is False

    def test_is_large_boundary_capacity_exactly_4(self):
        room_type = RoomType("Quad", 4, 100.0)
        assert room_type.is_large() is True

    def test_is_large_boundary_capacity_3(self):
        room_type = RoomType("Triple", 3, 100.0)
        assert room_type.is_large() is False

    def test_is_large_boundary_price_exactly_80(self):
        room_type = RoomType("Quad", 4, 80.0)
        assert room_type.is_large() is False

    def test_is_large_boundary_price_81(self):
        room_type = RoomType("Quad", 4, 81.0)
        assert room_type.is_large() is True

    def test_is_large_both_boundaries(self):
        room_type = RoomType("Room", 4, 80.0)
        assert room_type.is_large() is False

    def test_is_large_both_above_boundaries(self):
        room_type = RoomType("Room", 5, 85.0)
        assert room_type.is_large() is True

    def test_is_large_high_capacity_low_price(self):
        room_type = RoomType("Dorm", 10, 30.0)
        assert room_type.is_large() is False

    def test_is_large_low_capacity_high_price(self):
        room_type = RoomType("Luxury Single", 2, 500.0)
        assert room_type.is_large() is False

    def test_is_large_negative_values(self):
        room_type = RoomType("Invalid", -1, -100.0)
        assert room_type.is_large() is False

    def test_is_large_zero_values(self):
        room_type = RoomType("Empty", 0, 0.0)
        assert room_type.is_large() is False

    def test_calculate_price_precision(self):
        room_type = RoomType("Precise", 2, 123.456)
        price = room_type.calculate_price(1)
        # 123.456 + 12.3456 = 135.8016, rounded to 135.8
        assert price == 135.8

    def test_calculate_price_returns_float(self):
        room_type = RoomType("Standard", 2, 100.0)
        price = room_type.calculate_price(1)
        assert isinstance(price, float)

    def test_is_large_returns_boolean(self):
        room_type = RoomType("Standard", 2, 100.0)
        result = room_type.is_large()
        assert isinstance(result, bool)

    def test_calculate_price_consistency(self):
        room_type = RoomType("Standard", 2, 100.0)
        price1 = room_type.calculate_price(5)
        price2 = room_type.calculate_price(5)
        assert price1 == price2

    def test_is_large_consistency(self):
        room_type = RoomType("Suite", 4, 100.0)
        result1 = room_type.is_large()
        result2 = room_type.is_large()
        assert result1 == result2

    def test_calculate_price_does_not_modify_base_price(self):
        room_type = RoomType("Standard", 2, 100.0)
        original_price = room_type.base_price
        room_type.calculate_price(10)
        assert room_type.base_price == original_price

    def test_is_large_does_not_modify_attributes(self):
        room_type = RoomType("Suite", 4, 100.0)
        original_capacity = room_type.capacity
        original_price = room_type.base_price
        room_type.is_large()
        assert room_type.capacity == original_capacity
        assert room_type.base_price == original_price

    def test_calculate_price_single_night_formula(self):
        # Verify the exact formula: price = base_price + (base_price * 0.1) for 1 night
        room_type = RoomType("Test", 2, 50.0)
        price = room_type.calculate_price(1)
        expected = 50.0 + (50.0 * 0.1)
        assert price == round(expected, 2)
