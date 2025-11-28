import pytest
from services.ConferenceRoom import ConferenceRoom
from hotel_entities.Equipment import Equipment


class TestConferenceRoom:
    def test_init(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        assert room.code == "CR001"
        assert room.capacity == 50
        assert room.label == "Main Conference Hall"
        assert room.equipment == []

    def test_init_with_different_values(self):
        room = ConferenceRoom("CR002", 100, "Executive Boardroom")
        assert room.code == "CR002"
        assert room.capacity == 100
        assert room.label == "Executive Boardroom"

    def test_init_with_zero_capacity(self):
        room = ConferenceRoom("CR003", 0, "Small Meeting Room")
        assert room.capacity == 0
        assert room.equipment == []

    def test_add_equipment_valid(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        equipment = Equipment("Projector", "operational", "PRJ001")
        room.add_equipment(equipment)
        assert len(room.equipment) == 1
        assert room.equipment[0] == equipment
        assert room.capacity == 51

    def test_add_equipment_increases_capacity(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        initial_capacity = room.capacity
        equipment = Equipment("Projector", "operational", "PRJ001")
        room.add_equipment(equipment)
        assert room.capacity == initial_capacity + 1

    def test_add_multiple_equipment(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        eq1 = Equipment("Projector", "operational", "PRJ001")
        eq2 = Equipment("Microphone", "operational", "MIC001")
        eq3 = Equipment("Screen", "operational", "SCR001")
        room.add_equipment(eq1)
        room.add_equipment(eq2)
        room.add_equipment(eq3)
        assert len(room.equipment) == 3
        assert room.capacity == 53

    def test_add_equipment_invalid_type(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        with pytest.raises(ValueError, match="Invalid Equipment."):
            room.add_equipment("not an equipment")

    def test_add_equipment_none(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        with pytest.raises(ValueError, match="Invalid Equipment."):
            room.add_equipment(None)

    def test_add_equipment_invalid_object(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        with pytest.raises(ValueError, match="Invalid Equipment."):
            room.add_equipment({"name": "Projector"})

    def test_equipment_count_empty(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        assert room.equipment_count() == 0

    def test_equipment_count_single(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        equipment = Equipment("Projector", "operational", "PRJ001")
        room.add_equipment(equipment)
        assert room.equipment_count() == 1

    def test_equipment_count_multiple(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        eq1 = Equipment("Projector", "operational", "PRJ001")
        eq2 = Equipment("Microphone", "operational", "MIC001")
        eq3 = Equipment("Screen", "operational", "SCR001")
        room.add_equipment(eq1)
        room.add_equipment(eq2)
        room.add_equipment(eq3)
        assert room.equipment_count() == 3

    def test_equipment_count_consistency(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        assert room.equipment_count() == len(room.equipment)
        eq1 = Equipment("Projector", "operational", "PRJ001")
        room.add_equipment(eq1)
        assert room.equipment_count() == len(room.equipment)

    def test_add_same_equipment_multiple_times(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        equipment = Equipment("Projector", "operational", "PRJ001")
        room.add_equipment(equipment)
        room.add_equipment(equipment)
        assert room.equipment_count() == 2
        assert room.capacity == 52

    def test_capacity_calculation_with_different_equipment(self):
        room = ConferenceRoom("CR001", 50, "Main Conference Hall")
        for i in range(5):
            eq = Equipment(f"Equipment{i}", "operational", f"EQ00{i}")
            room.add_equipment(eq)
        assert room.capacity == 55
        assert room.equipment_count() == 5

    def test_empty_string_parameters(self):
        room = ConferenceRoom("", 50, "")
        assert room.code == ""
        assert room.label == ""
        assert room.capacity == 50

    def test_negative_capacity(self):
        room = ConferenceRoom("CR001", -10, "Small Room")
        assert room.capacity == -10
        equipment = Equipment("Projector", "operational", "PRJ001")
        room.add_equipment(equipment)
        assert room.capacity == -9
