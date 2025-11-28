import pytest
from hotel_entities.Facility import Facility


class TestFacility:
    def test_init(self):
        facility = Facility("Gym", "sports", 30)
        assert facility.name == "Gym"
        assert facility.category == "sports"
        assert facility.capacity == 30

    def test_init_with_zero_capacity(self):
        facility = Facility("Meeting Room", "business", 0)
        assert facility.name == "Meeting Room"
        assert facility.category == "business"
        assert facility.capacity == 0

    def test_init_with_negative_capacity(self):
        facility = Facility("Storage", "utility", -5)
        assert facility.capacity == -5

    def test_init_with_empty_strings(self):
        facility = Facility("", "", 10)
        assert facility.name == ""
        assert facility.category == ""

    def test_categorize_sport(self):
        facility = Facility("Gym", "sport", 30)
        assert facility.categorize() == "Recreational"

    def test_categorize_sports_plural(self):
        facility = Facility("Field", "sports", 100)
        assert facility.categorize() == "Recreational"

    def test_categorize_sport_uppercase(self):
        facility = Facility("Pool", "SPORTS", 50)
        assert facility.categorize() == "Recreational"

    def test_categorize_sport_mixedcase(self):
        facility = Facility("Court", "SpOrTs", 20)
        assert facility.categorize() == "Recreational"

    def test_categorize_sport_in_middle(self):
        facility = Facility("Area", "outdoor sport area", 40)
        assert facility.categorize() == "Recreational"

    def test_categorize_food(self):
        facility = Facility("Restaurant", "food", 100)
        assert facility.categorize() == "Dining"

    def test_categorize_food_uppercase(self):
        facility = Facility("Cafeteria", "FOOD", 80)
        assert facility.categorize() == "Dining"

    def test_categorize_food_mixedcase(self):
        facility = Facility("Bar", "FoOd", 50)
        assert facility.categorize() == "Dining"

    def test_categorize_food_in_middle(self):
        facility = Facility("Court", "fast food restaurant", 60)
        assert facility.categorize() == "Dining"

    def test_categorize_general(self):
        facility = Facility("Lobby", "general", 200)
        assert facility.categorize() == "General"

    def test_categorize_business(self):
        facility = Facility("Conference", "business", 50)
        assert facility.categorize() == "General"

    def test_categorize_empty_category(self):
        facility = Facility("Unknown", "", 30)
        assert facility.categorize() == "General"

    def test_categorize_unrelated_category(self):
        facility = Facility("Spa", "wellness", 25)
        assert facility.categorize() == "General"

    def test_categorize_sport_and_food(self):
        facility = Facility("Complex", "sport food court", 100)
        # "sport" appears first in the if checks
        assert facility.categorize() == "Recreational"

    def test_categorize_food_and_sport_reversed(self):
        facility = Facility("Complex", "food sport area", 100)
        # "sport" check comes first
        assert facility.categorize() == "Recreational"

    def test_is_large_true(self):
        facility = Facility("Arena", "sports", 100)
        assert facility.is_large() is True

    def test_is_large_false_small_capacity(self):
        facility = Facility("Room", "general", 30)
        assert facility.is_large() is False

    def test_is_large_boundary_exactly_50(self):
        facility = Facility("Hall", "general", 50)
        assert facility.is_large() is False

    def test_is_large_boundary_51(self):
        facility = Facility("Hall", "general", 51)
        assert facility.is_large() is True

    def test_is_large_zero_capacity(self):
        facility = Facility("Closet", "storage", 0)
        assert facility.is_large() is False

    def test_is_large_negative_capacity(self):
        facility = Facility("Virtual", "online", -10)
        assert facility.is_large() is False

    def test_is_large_exactly_threshold(self):
        facility = Facility("Medium Hall", "events", 50)
        assert facility.is_large() is False

    def test_is_large_one_above_threshold(self):
        facility = Facility("Large Hall", "events", 51)
        assert facility.is_large() is True

    def test_categorize_with_special_characters(self):
        facility = Facility("Gym", "sport&fitness", 30)
        assert facility.categorize() == "Recreational"

    def test_categorize_priority_sport_over_food(self):
        facility = Facility("Complex", "sportfood", 100)
        assert facility.categorize() == "Recreational"

    def test_capacity_large_value(self):
        facility = Facility("Stadium", "sports", 10000)
        assert facility.is_large() is True
        assert facility.capacity == 10000

    def test_multiple_categorize_calls(self):
        facility = Facility("Gym", "sports", 30)
        assert facility.categorize() == "Recreational"
        assert facility.categorize() == "Recreational"
        assert facility.category == "sports"

    def test_categorize_does_not_modify_category(self):
        facility = Facility("Restaurant", "food service", 100)
        original_category = facility.category
        facility.categorize()
        assert facility.category == original_category
