import pytest
from hotel_entities.Hotel import Hotel
from hotel_entities.Floor import Floor
from hotel_entities.Location import Location


class TestHotel:
    def test_init(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        assert hotel.name == "Grand Hotel"
        assert hotel.rating == 5
        assert hotel.address == "123 Main St"
        assert hotel.floors == []
        assert hotel.location is None

    def test_init_with_zero_rating(self):
        hotel = Hotel("Budget Inn", 0, "456 Side St")
        assert hotel.rating == 0

    def test_init_with_negative_rating(self):
        hotel = Hotel("Test Hotel", -1, "789 Back St")
        assert hotel.rating == -1

    def test_init_with_empty_strings(self):
        hotel = Hotel("", 3, "")
        assert hotel.name == ""
        assert hotel.address == ""

    def test_add_floor_valid(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor = Floor(1, "First Floor", True)
        hotel.add_floor(floor)
        assert len(hotel.floors) == 1
        assert hotel.floors[0] == floor

    def test_add_floor_invalid_type(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        with pytest.raises(ValueError, match="Only Floor instances allowed"):
            hotel.add_floor("not a floor")

    def test_add_floor_none(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        with pytest.raises(ValueError, match="Only Floor instances allowed"):
            hotel.add_floor(None)

    def test_add_floor_integer(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        with pytest.raises(ValueError, match="Only Floor instances allowed"):
            hotel.add_floor(1)

    def test_add_floor_dict(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        with pytest.raises(ValueError, match="Only Floor instances allowed"):
            hotel.add_floor({"number": 1})

    def test_add_floor_duplicate(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor = Floor(1, "First Floor", True)
        hotel.add_floor(floor)
        hotel.add_floor(floor)
        assert len(hotel.floors) == 1

    def test_add_multiple_floors(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor1 = Floor(1, "First Floor", True)
        floor2 = Floor(2, "Second Floor", True)
        floor3 = Floor(3, "Third Floor", True)
        hotel.add_floor(floor1)
        hotel.add_floor(floor2)
        hotel.add_floor(floor3)
        assert len(hotel.floors) == 3

    def test_add_floor_sorting(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor3 = Floor(3, "Third Floor", True)
        floor1 = Floor(1, "First Floor", True)
        floor2 = Floor(2, "Second Floor", True)
        hotel.add_floor(floor3)
        hotel.add_floor(floor1)
        hotel.add_floor(floor2)
        assert hotel.floors[0].number == 1
        assert hotel.floors[1].number == 2
        assert hotel.floors[2].number == 3

    def test_add_floor_reverse_order(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor5 = Floor(5, "Fifth", True)
        floor4 = Floor(4, "Fourth", True)
        floor3 = Floor(3, "Third", True)
        floor2 = Floor(2, "Second", True)
        floor1 = Floor(1, "First", True)
        hotel.add_floor(floor5)
        hotel.add_floor(floor4)
        hotel.add_floor(floor3)
        hotel.add_floor(floor2)
        hotel.add_floor(floor1)
        assert hotel.floors[0].number == 1
        assert hotel.floors[4].number == 5

    def test_add_floor_negative_numbers(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor_minus1 = Floor(-1, "Basement", True)
        floor_0 = Floor(0, "Ground", True)
        floor_1 = Floor(1, "First", True)
        hotel.add_floor(floor_1)
        hotel.add_floor(floor_minus1)
        hotel.add_floor(floor_0)
        assert hotel.floors[0].number == -1
        assert hotel.floors[1].number == 0
        assert hotel.floors[2].number == 1

    def test_set_location_valid(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        location = Location("New York", "USA", "Broadway")
        hotel.set_location(location)
        assert hotel.location == location

    def test_set_location_invalid_type(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        with pytest.raises(ValueError, match="Invalid location object"):
            hotel.set_location("not a location")

    def test_set_location_none(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        with pytest.raises(ValueError, match="Invalid location object"):
            hotel.set_location(None)

    def test_set_location_integer(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        with pytest.raises(ValueError, match="Invalid location object"):
            hotel.set_location(123)

    def test_set_location_dict(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        with pytest.raises(ValueError, match="Invalid location object"):
            hotel.set_location({"city": "New York"})

    def test_set_location_updates_address_with_city(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        location = Location("New York", "USA", "Broadway")
        hotel.set_location(location)
        assert "New York" in hotel.address
        assert "123 Main St" in hotel.address

    def test_set_location_address_format(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        location = Location("Paris", "France", "Champs-Élysées")
        hotel.set_location(location)
        assert hotel.address == "Paris, 123 Main St"

    def test_set_location_multiple_times(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        location1 = Location("New York", "USA", "Broadway")
        location2 = Location("Paris", "France", "Champs-Élysées")
        hotel.set_location(location1)
        first_address = hotel.address
        hotel.set_location(location2)
        assert hotel.location == location2
        assert hotel.address == "Paris, " + first_address

    def test_set_location_without_city_attribute(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        # Create a mock object without city attribute
        class MockLocation:
            pass
        mock_location = MockLocation()
        with pytest.raises(ValueError, match="Invalid location object"):
            hotel.set_location(mock_location)

    def test_set_location_with_city_attribute(self):
        hotel = Hotel("Grand Hotel", 5, "Original Address")
        location = Location("Tokyo", "Japan", "Shibuya")
        original_address = hotel.address
        hotel.set_location(location)
        assert hotel.address == f"Tokyo, {original_address}"

    def test_location_initial_state(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        assert hotel.location is None

    def test_add_floor_and_set_location(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor = Floor(1, "First Floor", True)
        location = Location("London", "UK", "Baker Street")
        hotel.add_floor(floor)
        hotel.set_location(location)
        assert len(hotel.floors) == 1
        assert hotel.location == location
        assert "London" in hotel.address

    def test_add_floors_with_duplicate_numbers(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor1a = Floor(1, "First A", True)
        floor1b = Floor(1, "First B", False)
        hotel.add_floor(floor1a)
        hotel.add_floor(floor1b)
        # Both should be added as they are different objects
        assert len(hotel.floors) == 2

    def test_add_floor_maintains_sort_after_insertion(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        floor1 = Floor(1, "First", True)
        floor3 = Floor(3, "Third", True)
        hotel.add_floor(floor1)
        hotel.add_floor(floor3)
        floor2 = Floor(2, "Second", True)
        hotel.add_floor(floor2)
        assert hotel.floors[0].number == 1
        assert hotel.floors[1].number == 2
        assert hotel.floors[2].number == 3

    def test_high_rating(self):
        hotel = Hotel("Luxury Resort", 10, "Beach Road")
        assert hotel.rating == 10

    def test_location_city_attribute_check(self):
        hotel = Hotel("Grand Hotel", 5, "123 Main St")
        location = Location("Berlin", "Germany", "Unter den Linden")
        assert hasattr(location, "city")
        hotel.set_location(location)
        assert "Berlin" in hotel.address
