import pytest
from hotel_entities.Amenity import Amenity


class TestAmenity:
    def test_init(self):
        amenity = Amenity("WiFi", "High-speed internet", 10.0)
        assert amenity.name == "WiFi"
        assert amenity.description == "High-speed internet"
        assert amenity.cost == 10.0

    def test_init_with_zero_cost(self):
        amenity = Amenity("Pool", "Swimming pool access", 0.0)
        assert amenity.name == "Pool"
        assert amenity.description == "Swimming pool access"
        assert amenity.cost == 0.0

    def test_init_with_negative_cost(self):
        amenity = Amenity("Breakfast", "Complimentary breakfast", -5.0)
        assert amenity.name == "Breakfast"
        assert amenity.description == "Complimentary breakfast"
        assert amenity.cost == -5.0

    def test_detailed_info_basic(self):
        amenity = Amenity("WiFi", "High-speed internet", 10.0)
        result = amenity.detailed_info()
        assert result == "Wifi - High-speed Internet ($10.0)"

    def test_detailed_info_capitalizes_words(self):
        amenity = Amenity("spa access", "luxury spa treatment", 50.0)
        result = amenity.detailed_info()
        assert result == "Spa Access - Luxury Spa Treatment ($50.0)"

    def test_detailed_info_with_zero_cost(self):
        amenity = Amenity("Parking", "Free parking", 0.0)
        result = amenity.detailed_info()
        assert result == "Parking - Free Parking ($0.0)"

    def test_detailed_info_with_negative_cost(self):
        amenity = Amenity("Discount", "Special discount", -10.0)
        result = amenity.detailed_info()
        assert result == "Discount - Special Discount ($-10.0)"

    def test_detailed_info_with_special_characters(self):
        amenity = Amenity("Room-Service", "24/7 room service", 25.5)
        result = amenity.detailed_info()
        assert result == "Room-service - 24/7 Room Service ($25.5)"

    def test_is_free_with_zero_cost(self):
        amenity = Amenity("Pool", "Swimming pool access", 0.0)
        assert amenity.is_free() is True

    def test_is_free_with_negative_cost(self):
        amenity = Amenity("Discount", "Special discount", -5.0)
        assert amenity.is_free() is True

    def test_is_free_with_positive_cost(self):
        amenity = Amenity("WiFi", "High-speed internet", 10.0)
        assert amenity.is_free() is False

    def test_is_free_with_small_positive_cost(self):
        amenity = Amenity("Water", "Bottled water", 0.01)
        assert amenity.is_free() is False

    def test_is_free_boundary_case(self):
        amenity = Amenity("Service", "Free service", 0.0)
        assert amenity.is_free() is True

    def test_detailed_info_with_empty_strings(self):
        amenity = Amenity("", "", 5.0)
        result = amenity.detailed_info()
        # Empty strings when split create empty list, join creates just "- ($5.0)"
        assert result == "- ($5.0)"

    def test_detailed_info_with_single_word(self):
        amenity = Amenity("Gym", "Gym", 15.0)
        result = amenity.detailed_info()
        assert result == "Gym - Gym ($15.0)"

    def test_multiple_spaces_in_detailed_info(self):
        amenity = Amenity("spa  service", "luxury  treatment", 100.0)
        result = amenity.detailed_info()
        # Multiple spaces are preserved and each word is capitalized
        assert "Spa" in result and "Service" in result

    def test_cost_precision(self):
        amenity = Amenity("Service", "Test", 10.999)
        assert amenity.cost == 10.999

    def test_is_free_with_very_small_positive_cost(self):
        amenity = Amenity("Service", "Test", 0.0001)
        assert amenity.is_free() is False
