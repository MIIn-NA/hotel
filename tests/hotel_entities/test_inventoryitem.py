import pytest
from hotel_entities.InventoryItem import InventoryItem


class TestInventoryItem:
    def test_init(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        assert item.name == "Towel"
        assert item.quantity == 100
        assert item.code == "TWL-001"

    def test_init_with_zero_quantity(self):
        item = InventoryItem("Soap", 0, "SOP-001")
        assert item.quantity == 0

    def test_init_with_negative_quantity(self):
        item = InventoryItem("Item", -5, "ITM-001")
        assert item.quantity == -5

    def test_init_with_empty_strings(self):
        item = InventoryItem("", 50, "")
        assert item.name == ""
        assert item.code == ""

    def test_use_valid_amount(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        item.use(30)
        assert item.quantity == 70

    def test_use_zero_amount(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        item.use(0)
        assert item.quantity == 100

    def test_use_exact_quantity(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        item.use(100)
        assert item.quantity == 0

    def test_use_more_than_available(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        item.use(150)
        assert item.quantity == 0

    def test_use_negative_amount(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        with pytest.raises(ValueError, match="Amount cannot be negative"):
            item.use(-10)

    def test_use_small_amount(self):
        item = InventoryItem("Soap", 50, "SOP-001")
        item.use(1)
        assert item.quantity == 49

    def test_use_multiple_times(self):
        item = InventoryItem("Shampoo", 100, "SHP-001")
        item.use(20)
        item.use(30)
        item.use(10)
        assert item.quantity == 40

    def test_use_until_depleted(self):
        item = InventoryItem("Soap", 10, "SOP-001")
        item.use(5)
        item.use(5)
        assert item.quantity == 0

    def test_use_after_depleted(self):
        item = InventoryItem("Soap", 10, "SOP-001")
        item.use(10)
        item.use(5)
        assert item.quantity == 0

    def test_restock_valid_amount(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        item.restock(50)
        assert item.quantity == 150

    def test_restock_small_amount(self):
        item = InventoryItem("Soap", 20, "SOP-001")
        item.restock(1)
        assert item.quantity == 21

    def test_restock_large_amount(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        item.restock(1000)
        assert item.quantity == 1100

    def test_restock_zero_amount(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        with pytest.raises(ValueError, match="Invalid restock amount"):
            item.restock(0)

    def test_restock_negative_amount(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        with pytest.raises(ValueError, match="Invalid restock amount"):
            item.restock(-10)

    def test_restock_after_use(self):
        item = InventoryItem("Shampoo", 100, "SHP-001")
        item.use(50)
        item.restock(30)
        assert item.quantity == 80

    def test_use_after_restock(self):
        item = InventoryItem("Soap", 50, "SOP-001")
        item.restock(50)
        item.use(30)
        assert item.quantity == 70

    def test_multiple_restocks(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        item.restock(25)
        item.restock(25)
        item.restock(50)
        assert item.quantity == 200

    def test_use_and_restock_cycle(self):
        item = InventoryItem("Soap", 100, "SOP-001")
        item.use(30)  # 70
        item.restock(50)  # 120
        item.use(20)  # 100
        item.restock(10)  # 110
        assert item.quantity == 110

    def test_use_depletes_then_restock(self):
        item = InventoryItem("Towel", 50, "TWL-001")
        item.use(60)  # More than available, sets to 0
        assert item.quantity == 0
        item.restock(100)
        assert item.quantity == 100

    def test_quantity_never_negative_after_use(self):
        item = InventoryItem("Item", 10, "ITM-001")
        item.use(100)
        assert item.quantity == 0
        assert item.quantity >= 0

    def test_use_boundary_one_less(self):
        item = InventoryItem("Item", 100, "ITM-001")
        item.use(99)
        assert item.quantity == 1

    def test_use_boundary_one_more(self):
        item = InventoryItem("Item", 100, "ITM-001")
        item.use(101)
        assert item.quantity == 0

    def test_restock_from_zero(self):
        item = InventoryItem("Item", 0, "ITM-001")
        item.restock(50)
        assert item.quantity == 50

    def test_use_with_float_amount_if_passed(self):
        item = InventoryItem("Item", 100, "ITM-001")
        item.use(10.5)
        assert item.quantity == 89.5

    def test_restock_with_float_amount_if_passed(self):
        item = InventoryItem("Item", 100, "ITM-001")
        item.restock(10.5)
        assert item.quantity == 110.5

    def test_code_preservation(self):
        item = InventoryItem("Towel", 100, "TWL-001")
        item.use(50)
        item.restock(25)
        assert item.code == "TWL-001"

    def test_name_preservation(self):
        item = InventoryItem("Luxury Towel", 100, "LTW-001")
        item.use(50)
        item.restock(25)
        assert item.name == "Luxury Towel"
