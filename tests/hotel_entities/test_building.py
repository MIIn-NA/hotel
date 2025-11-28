import pytest
from hotel_entities.Building import Building
from hotel_entities.Facility import Facility


class TestBuilding:
    def test_init(self):
        building = Building("Main Building", 10, "MB01")
        assert building.name == "Main Building"
        assert building.floors == 10
        assert building.code == "MB01"
        assert building.facilities == []

    def test_init_with_zero_floors(self):
        building = Building("Annex", 0, "ANX01")
        assert building.name == "Annex"
        assert building.floors == 0
        assert building.code == "ANX01"

    def test_init_with_negative_floors(self):
        building = Building("Underground", -1, "UG01")
        assert building.floors == -1

    def test_add_facility_valid(self):
        building = Building("Main", 5, "M01")
        facility = Facility("Gym", "sports", 30)
        building.add_facility(facility)
        assert len(building.facilities) == 1
        assert building.facilities[0] == facility

    def test_add_facility_invalid_type(self):
        building = Building("Main", 5, "M01")
        with pytest.raises(ValueError, match="Invalid Facility object"):
            building.add_facility("not a facility")

    def test_add_facility_duplicate(self):
        building = Building("Main", 5, "M01")
        facility = Facility("Gym", "sports", 30)
        building.add_facility(facility)
        building.add_facility(facility)
        assert len(building.facilities) == 1

    def test_add_multiple_facilities(self):
        building = Building("Main", 5, "M01")
        facility1 = Facility("Gym", "sports", 30)
        facility2 = Facility("Pool", "sports", 50)
        facility3 = Facility("Restaurant", "food", 100)
        building.add_facility(facility1)
        building.add_facility(facility2)
        building.add_facility(facility3)
        assert len(building.facilities) == 3

    def test_add_facility_none(self):
        building = Building("Main", 5, "M01")
        with pytest.raises(ValueError, match="Invalid Facility object"):
            building.add_facility(None)

    def test_floor_density_no_facilities(self):
        building = Building("Main", 5, "M01")
        assert building.floor_density() == 0.0

    def test_floor_density_with_facilities(self):
        building = Building("Main", 10, "M01")
        facility1 = Facility("Gym", "sports", 30)
        facility2 = Facility("Pool", "sports", 50)
        building.add_facility(facility1)
        building.add_facility(facility2)
        assert building.floor_density() == 0.2

    def test_floor_density_zero_floors(self):
        building = Building("Main", 0, "M01")
        facility = Facility("Gym", "sports", 30)
        building.add_facility(facility)
        assert building.floor_density() == 0.0

    def test_floor_density_rounding(self):
        building = Building("Main", 3, "M01")
        facility1 = Facility("Gym", "sports", 30)
        facility2 = Facility("Pool", "sports", 50)
        building.add_facility(facility1)
        building.add_facility(facility2)
        # 2/3 = 0.666... should round to 0.67
        assert building.floor_density() == 0.67

    def test_floor_density_exact_division(self):
        building = Building("Main", 2, "M01")
        facility1 = Facility("Gym", "sports", 30)
        facility2 = Facility("Pool", "sports", 50)
        building.add_facility(facility1)
        building.add_facility(facility2)
        assert building.floor_density() == 1.0

    def test_floor_density_more_facilities_than_floors(self):
        building = Building("Main", 2, "M01")
        facility1 = Facility("Gym", "sports", 30)
        facility2 = Facility("Pool", "sports", 50)
        facility3 = Facility("Restaurant", "food", 100)
        building.add_facility(facility1)
        building.add_facility(facility2)
        building.add_facility(facility3)
        assert building.floor_density() == 1.5

    def test_floor_density_single_facility(self):
        building = Building("Main", 1, "M01")
        facility = Facility("Gym", "sports", 30)
        building.add_facility(facility)
        assert building.floor_density() == 1.0

    def test_init_with_empty_strings(self):
        building = Building("", 5, "")
        assert building.name == ""
        assert building.code == ""
        assert building.floors == 5

    def test_add_facility_integer_raises_error(self):
        building = Building("Main", 5, "M01")
        with pytest.raises(ValueError, match="Invalid Facility object"):
            building.add_facility(123)

    def test_add_facility_dict_raises_error(self):
        building = Building("Main", 5, "M01")
        with pytest.raises(ValueError, match="Invalid Facility object"):
            building.add_facility({"name": "Gym"})

    def test_floor_density_with_one_floor_multiple_facilities(self):
        building = Building("Main", 1, "M01")
        for i in range(5):
            facility = Facility(f"Facility{i}", "general", 10)
            building.add_facility(facility)
        assert building.floor_density() == 5.0

    def test_floor_density_precision(self):
        building = Building("Main", 7, "M01")
        for i in range(5):
            facility = Facility(f"Facility{i}", "general", 10)
            building.add_facility(facility)
        # 5/7 = 0.714285... should round to 0.71
        assert building.floor_density() == 0.71
