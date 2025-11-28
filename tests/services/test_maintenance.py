import pytest
from services.Maintenance import Maintenance
from hotel_entities.Equipment import Equipment


class TestMaintenance:
    def test_init(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        assert maintenance.technician == "Bob Wilson"
        assert maintenance.date == "2024-12-01"
        assert maintenance.category == "routine"
        assert maintenance.equipment == []

    def test_init_with_different_values(self):
        maintenance = Maintenance("Alice Brown", "2024-11-15", "emergency")
        assert maintenance.technician == "Alice Brown"
        assert maintenance.date == "2024-11-15"
        assert maintenance.category == "emergency"

    def test_init_empty_equipment_list(self):
        maintenance = Maintenance("Technician", "2024-10-10", "scheduled")
        assert maintenance.equipment == []
        assert len(maintenance.equipment) == 0

    def test_register_equipment_valid(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        equipment = Equipment("Air Conditioner", "operational", "AC001")
        maintenance.register_equipment(equipment)
        assert len(maintenance.equipment) == 1
        assert maintenance.equipment[0] == equipment
        assert equipment.status == "maintenance"

    def test_register_equipment_changes_status(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        equipment = Equipment("Air Conditioner", "operational", "AC001")
        assert equipment.status == "operational"
        maintenance.register_equipment(equipment)
        assert equipment.status == "maintenance"

    def test_register_equipment_already_in_maintenance(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        equipment = Equipment("Heater", "maintenance", "HT001")
        maintenance.register_equipment(equipment)
        assert equipment.status == "maintenance"
        assert len(maintenance.equipment) == 1

    def test_register_multiple_equipment(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        eq1 = Equipment("Air Conditioner", "operational", "AC001")
        eq2 = Equipment("Heater", "operational", "HT001")
        eq3 = Equipment("Elevator", "operational", "EL001")
        maintenance.register_equipment(eq1)
        maintenance.register_equipment(eq2)
        maintenance.register_equipment(eq3)
        assert len(maintenance.equipment) == 3
        assert eq1.status == "maintenance"
        assert eq2.status == "maintenance"
        assert eq3.status == "maintenance"

    def test_register_equipment_invalid_type(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        with pytest.raises(ValueError, match="Invalid Equipment."):
            maintenance.register_equipment("not equipment")

    def test_register_equipment_none(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        with pytest.raises(ValueError, match="Invalid Equipment."):
            maintenance.register_equipment(None)

    def test_register_equipment_invalid_object(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        with pytest.raises(ValueError, match="Invalid Equipment."):
            maintenance.register_equipment({"name": "AC"})

    def test_register_same_equipment_multiple_times(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        equipment = Equipment("Air Conditioner", "operational", "AC001")
        maintenance.register_equipment(equipment)
        maintenance.register_equipment(equipment)
        assert len(maintenance.equipment) == 2
        assert equipment.status == "maintenance"

    def test_total_items_empty(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        assert maintenance.total_items() == 0

    def test_total_items_single(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        equipment = Equipment("Air Conditioner", "operational", "AC001")
        maintenance.register_equipment(equipment)
        assert maintenance.total_items() == 1

    def test_total_items_multiple(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        eq1 = Equipment("Air Conditioner", "operational", "AC001")
        eq2 = Equipment("Heater", "operational", "HT001")
        eq3 = Equipment("Elevator", "operational", "EL001")
        maintenance.register_equipment(eq1)
        maintenance.register_equipment(eq2)
        maintenance.register_equipment(eq3)
        assert maintenance.total_items() == 3

    def test_total_items_consistency(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        assert maintenance.total_items() == len(maintenance.equipment)
        equipment = Equipment("AC", "operational", "AC001")
        maintenance.register_equipment(equipment)
        assert maintenance.total_items() == len(maintenance.equipment)

    def test_empty_string_parameters(self):
        maintenance = Maintenance("", "", "")
        assert maintenance.technician == ""
        assert maintenance.date == ""
        assert maintenance.category == ""

    def test_register_equipment_with_different_statuses(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        eq1 = Equipment("AC", "operational", "AC001")
        eq2 = Equipment("Heater", "broken", "HT001")
        eq3 = Equipment("Elevator", "maintenance", "EL001")
        maintenance.register_equipment(eq1)
        maintenance.register_equipment(eq2)
        maintenance.register_equipment(eq3)
        assert eq1.status == "maintenance"
        assert eq2.status == "maintenance"
        assert eq3.status == "maintenance"

    def test_multiple_maintenance_sessions_same_equipment(self):
        maintenance1 = Maintenance("Bob Wilson", "2024-12-01", "routine")
        maintenance2 = Maintenance("Alice Brown", "2024-12-02", "emergency")
        equipment = Equipment("AC", "operational", "AC001")
        maintenance1.register_equipment(equipment)
        assert maintenance1.total_items() == 1
        assert equipment.status == "maintenance"
        maintenance2.register_equipment(equipment)
        assert maintenance2.total_items() == 1
        assert equipment.status == "maintenance"

    def test_register_equipment_preserves_order(self):
        maintenance = Maintenance("Bob Wilson", "2024-12-01", "routine")
        eq1 = Equipment("AC", "operational", "AC001")
        eq2 = Equipment("Heater", "operational", "HT001")
        eq3 = Equipment("Elevator", "operational", "EL001")
        maintenance.register_equipment(eq1)
        maintenance.register_equipment(eq2)
        maintenance.register_equipment(eq3)
        assert maintenance.equipment[0] == eq1
        assert maintenance.equipment[1] == eq2
        assert maintenance.equipment[2] == eq3
