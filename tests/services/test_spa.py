import pytest
from services.Spa import Spa
from services.Treatment import Treatment


class TestSpa:
    def test_init(self):
        spa = Spa("Relaxation Haven", 500, 8)
        assert spa.name == "Relaxation Haven"
        assert spa.area == 500
        assert spa.rating == 8
        assert spa.treatments == []

    def test_init_with_different_values(self):
        spa = Spa("Wellness Center", 300, 5)
        assert spa.name == "Wellness Center"
        assert spa.area == 300
        assert spa.rating == 5

    def test_init_with_zero_rating(self):
        spa = Spa("New Spa", 200, 0)
        assert spa.rating == 0
        assert spa.treatments == []

    def test_init_with_max_rating(self):
        spa = Spa("Premium Spa", 1000, 10)
        assert spa.rating == 10

    def test_add_treatment_valid(self):
        spa = Spa("Relaxation Haven", 500, 8)
        treatment = Treatment("Swedish Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert len(spa.treatments) == 1
        assert spa.treatments[0] == treatment
        assert spa.rating == 9

    def test_add_treatment_increases_rating(self):
        spa = Spa("Relaxation Haven", 500, 5)
        treatment = Treatment("Swedish Massage", 60, 100.0)
        initial_rating = spa.rating
        spa.add_treatment(treatment)
        assert spa.rating == initial_rating + 1

    def test_add_treatment_rating_caps_at_10(self):
        spa = Spa("Premium Spa", 1000, 10)
        treatment = Treatment("Swedish Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert spa.rating == 10

    def test_add_treatment_rating_approaches_10(self):
        spa = Spa("Relaxation Haven", 500, 9)
        treatment = Treatment("Swedish Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert spa.rating == 10

    def test_add_multiple_treatments(self):
        spa = Spa("Relaxation Haven", 500, 5)
        t1 = Treatment("Swedish Massage", 60, 100.0)
        t2 = Treatment("Hot Stone Therapy", 90, 150.0)
        t3 = Treatment("Aromatherapy", 45, 80.0)
        spa.add_treatment(t1)
        spa.add_treatment(t2)
        spa.add_treatment(t3)
        assert len(spa.treatments) == 3
        assert spa.rating == 8

    def test_add_multiple_treatments_rating_caps(self):
        spa = Spa("Relaxation Haven", 500, 8)
        for i in range(5):
            treatment = Treatment(f"Treatment {i}", 60, 100.0)
            spa.add_treatment(treatment)
        assert spa.rating == 10
        assert len(spa.treatments) == 5

    def test_add_treatment_invalid_type(self):
        spa = Spa("Relaxation Haven", 500, 8)
        with pytest.raises(ValueError, match="Invalid treatment."):
            spa.add_treatment("not a treatment")

    def test_add_treatment_none(self):
        spa = Spa("Relaxation Haven", 500, 8)
        with pytest.raises(ValueError, match="Invalid treatment."):
            spa.add_treatment(None)

    def test_add_treatment_invalid_object(self):
        spa = Spa("Relaxation Haven", 500, 8)
        with pytest.raises(ValueError, match="Invalid treatment."):
            spa.add_treatment({"name": "Massage"})

    def test_add_same_treatment_multiple_times(self):
        spa = Spa("Relaxation Haven", 500, 5)
        treatment = Treatment("Swedish Massage", 60, 100.0)
        spa.add_treatment(treatment)
        spa.add_treatment(treatment)
        assert len(spa.treatments) == 2
        assert spa.rating == 7

    def test_treatment_count_empty(self):
        spa = Spa("Relaxation Haven", 500, 8)
        assert spa.treatment_count() == 0

    def test_treatment_count_single(self):
        spa = Spa("Relaxation Haven", 500, 8)
        treatment = Treatment("Swedish Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert spa.treatment_count() == 1

    def test_treatment_count_multiple(self):
        spa = Spa("Relaxation Haven", 500, 8)
        t1 = Treatment("Swedish Massage", 60, 100.0)
        t2 = Treatment("Hot Stone Therapy", 90, 150.0)
        t3 = Treatment("Aromatherapy", 45, 80.0)
        spa.add_treatment(t1)
        spa.add_treatment(t2)
        spa.add_treatment(t3)
        assert spa.treatment_count() == 3

    def test_treatment_count_consistency(self):
        spa = Spa("Relaxation Haven", 500, 8)
        assert spa.treatment_count() == len(spa.treatments)
        treatment = Treatment("Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert spa.treatment_count() == len(spa.treatments)

    def test_empty_string_parameters(self):
        spa = Spa("", 0, 0)
        assert spa.name == ""
        assert spa.area == 0
        assert spa.rating == 0

    def test_negative_area(self):
        spa = Spa("Spa", -100, 5)
        assert spa.area == -100

    def test_negative_rating(self):
        spa = Spa("Spa", 500, -5)
        assert spa.rating == -5
        treatment = Treatment("Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert spa.rating == -4

    def test_rating_above_10_initial(self):
        spa = Spa("Spa", 500, 15)
        assert spa.rating == 15
        treatment = Treatment("Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert spa.rating == 10

    def test_add_treatment_preserves_order(self):
        spa = Spa("Relaxation Haven", 500, 5)
        t1 = Treatment("Treatment A", 60, 100.0)
        t2 = Treatment("Treatment B", 90, 150.0)
        t3 = Treatment("Treatment C", 45, 80.0)
        spa.add_treatment(t1)
        spa.add_treatment(t2)
        spa.add_treatment(t3)
        assert spa.treatments[0] == t1
        assert spa.treatments[1] == t2
        assert spa.treatments[2] == t3

    def test_add_treatments_with_different_durations(self):
        spa = Spa("Relaxation Haven", 500, 5)
        t1 = Treatment("Quick Massage", 30, 50.0)
        t2 = Treatment("Standard Massage", 60, 100.0)
        t3 = Treatment("Extended Massage", 120, 200.0)
        spa.add_treatment(t1)
        spa.add_treatment(t2)
        spa.add_treatment(t3)
        assert spa.treatment_count() == 3

    def test_add_treatments_with_different_prices(self):
        spa = Spa("Relaxation Haven", 500, 5)
        t1 = Treatment("Budget Massage", 60, 50.0)
        t2 = Treatment("Premium Massage", 60, 200.0)
        t3 = Treatment("Luxury Massage", 60, 500.0)
        spa.add_treatment(t1)
        spa.add_treatment(t2)
        spa.add_treatment(t3)
        assert spa.treatment_count() == 3

    def test_rating_increment_from_zero(self):
        spa = Spa("New Spa", 500, 0)
        for i in range(12):
            treatment = Treatment(f"Treatment {i}", 60, 100.0)
            spa.add_treatment(treatment)
        assert spa.rating == 10
        assert spa.treatment_count() == 12

    def test_rating_at_boundary_9(self):
        spa = Spa("Spa", 500, 9)
        assert spa.rating == 9
        treatment = Treatment("Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert spa.rating == 10

    def test_min_function_with_rating_11(self):
        spa = Spa("Spa", 500, 11)
        treatment = Treatment("Massage", 60, 100.0)
        spa.add_treatment(treatment)
        assert spa.rating == 10
