import pytest
from hotel_entities.Equipment import Equipment


class TestEquipment:
    def test_init(self):
        equipment = Equipment("Vacuum Cleaner", "operational", "VC-001")
        assert equipment.name == "Vacuum Cleaner"
        assert equipment.status == "operational"
        assert equipment.serial == "VC-001"

    def test_init_with_different_status(self):
        equipment = Equipment("Air Conditioner", "broken", "AC-123")
        assert equipment.name == "Air Conditioner"
        assert equipment.status == "broken"
        assert equipment.serial == "AC-123"

    def test_init_with_empty_strings(self):
        equipment = Equipment("", "", "")
        assert equipment.name == ""
        assert equipment.status == ""
        assert equipment.serial == ""

    def test_mark_repaired_from_broken(self):
        equipment = Equipment("Dishwasher", "broken", "DW-001")
        equipment.mark_repaired()
        assert equipment.status == "operational"

    def test_mark_repaired_from_broken_uppercase(self):
        equipment = Equipment("Dishwasher", "BROKEN", "DW-001")
        equipment.mark_repaired()
        assert equipment.status == "operational"

    def test_mark_repaired_from_broken_mixedcase(self):
        equipment = Equipment("Dishwasher", "BrOkEn", "DW-001")
        equipment.mark_repaired()
        assert equipment.status == "operational"

    def test_mark_repaired_from_operational(self):
        equipment = Equipment("Dishwasher", "operational", "DW-001")
        equipment.mark_repaired()
        assert equipment.status == "operational"

    def test_mark_repaired_from_other_status(self):
        equipment = Equipment("Dishwasher", "maintenance", "DW-001")
        equipment.mark_repaired()
        assert equipment.status == "maintenance"

    def test_mark_repaired_from_empty_status(self):
        equipment = Equipment("Dishwasher", "", "DW-001")
        equipment.mark_repaired()
        assert equipment.status == ""

    def test_mark_broken(self):
        equipment = Equipment("Vacuum", "operational", "VC-001")
        equipment.mark_broken()
        assert equipment.status == "broken"

    def test_mark_broken_from_broken(self):
        equipment = Equipment("Vacuum", "broken", "VC-001")
        equipment.mark_broken()
        assert equipment.status == "broken"

    def test_mark_broken_from_maintenance(self):
        equipment = Equipment("Vacuum", "maintenance", "VC-001")
        equipment.mark_broken()
        assert equipment.status == "broken"

    def test_mark_broken_from_empty_status(self):
        equipment = Equipment("Vacuum", "", "VC-001")
        equipment.mark_broken()
        assert equipment.status == "broken"

    def test_mark_broken_then_repaired(self):
        equipment = Equipment("Dryer", "operational", "DR-001")
        equipment.mark_broken()
        assert equipment.status == "broken"
        equipment.mark_repaired()
        assert equipment.status == "operational"

    def test_mark_repaired_then_broken(self):
        equipment = Equipment("Washer", "broken", "WH-001")
        equipment.mark_repaired()
        assert equipment.status == "operational"
        equipment.mark_broken()
        assert equipment.status == "broken"

    def test_multiple_mark_broken_calls(self):
        equipment = Equipment("TV", "operational", "TV-001")
        equipment.mark_broken()
        equipment.mark_broken()
        equipment.mark_broken()
        assert equipment.status == "broken"

    def test_multiple_mark_repaired_calls_on_broken(self):
        equipment = Equipment("Microwave", "broken", "MW-001")
        equipment.mark_repaired()
        equipment.mark_repaired()
        equipment.mark_repaired()
        assert equipment.status == "operational"

    def test_mark_repaired_with_broken_in_middle_of_status(self):
        equipment = Equipment("Item", "notbrokenyet", "IT-001")
        equipment.mark_repaired()
        # lower() makes it "notbrokenyet" which != "broken" (exact match required)
        # So status should remain unchanged
        assert equipment.status == "notbrokenyet"

    def test_mark_repaired_case_sensitivity(self):
        equipment = Equipment("Item", "Broken", "IT-001")
        equipment.mark_repaired()
        # lower() makes it "broken" which == "broken", so it changes to operational
        assert equipment.status == "operational"

    def test_serial_number_preservation(self):
        equipment = Equipment("Fridge", "operational", "FR-12345")
        equipment.mark_broken()
        equipment.mark_repaired()
        assert equipment.serial == "FR-12345"

    def test_name_preservation(self):
        equipment = Equipment("Coffee Machine", "operational", "CM-001")
        equipment.mark_broken()
        equipment.mark_repaired()
        assert equipment.name == "Coffee Machine"

    def test_status_cycle(self):
        equipment = Equipment("Tool", "operational", "TL-001")
        original_status = equipment.status
        equipment.mark_broken()
        assert equipment.status != original_status
        equipment.mark_repaired()
        assert equipment.status == original_status
