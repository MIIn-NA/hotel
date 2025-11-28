import pytest
from services.Menu import Menu


class TestMenu:
    def test_init(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        assert menu.title == "Breakfast Menu"
        assert menu.description == "Morning delights"
        assert menu.code == "MN001"
        assert menu.items == []

    def test_init_with_different_values(self):
        menu = Menu("Dinner Menu", "Evening specials", "MN002")
        assert menu.title == "Dinner Menu"
        assert menu.description == "Evening specials"
        assert menu.code == "MN002"

    def test_init_empty_items_list(self):
        menu = Menu("Lunch Menu", "Afternoon choices", "MN003")
        assert menu.items == []
        assert len(menu.items) == 0

    def test_add_item_valid(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("Pancakes")
        assert len(menu.items) == 1
        assert menu.items[0] == "Pancakes"

    def test_add_item_strips_whitespace(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("  Pancakes  ")
        assert menu.items[0] == "Pancakes"
        assert menu.items[0] == "Pancakes"

    def test_add_item_with_leading_whitespace(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("   Eggs Benedict")
        assert menu.items[0] == "Eggs Benedict"

    def test_add_item_with_trailing_whitespace(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("French Toast   ")
        assert menu.items[0] == "French Toast"

    def test_add_multiple_items(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("Pancakes")
        menu.add_item("Eggs Benedict")
        menu.add_item("French Toast")
        assert len(menu.items) == 3
        assert "Pancakes" in menu.items
        assert "Eggs Benedict" in menu.items
        assert "French Toast" in menu.items

    def test_add_item_too_short(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        with pytest.raises(ValueError, match="Invalid menu item."):
            menu.add_item("A")

    def test_add_item_single_character(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        with pytest.raises(ValueError, match="Invalid menu item."):
            menu.add_item("X")

    def test_add_item_empty_string(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        with pytest.raises(ValueError, match="Invalid menu item."):
            menu.add_item("")

    def test_add_item_whitespace_only(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        with pytest.raises(ValueError, match="Invalid menu item."):
            menu.add_item("   ")

    def test_add_item_two_characters_valid(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("AB")
        assert len(menu.items) == 1
        assert menu.items[0] == "AB"

    def test_add_item_two_characters_with_whitespace(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("  AB  ")
        assert len(menu.items) == 1
        assert menu.items[0] == "AB"

    def test_add_item_single_char_after_strip(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        with pytest.raises(ValueError, match="Invalid menu item."):
            menu.add_item("  A  ")

    def test_add_same_item_multiple_times(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("Pancakes")
        menu.add_item("Pancakes")
        assert len(menu.items) == 2
        assert menu.items[0] == "Pancakes"
        assert menu.items[1] == "Pancakes"

    def test_item_count_empty(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        assert menu.item_count() == 0

    def test_item_count_single(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("Pancakes")
        assert menu.item_count() == 1

    def test_item_count_multiple(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("Pancakes")
        menu.add_item("Eggs Benedict")
        menu.add_item("French Toast")
        assert menu.item_count() == 3

    def test_item_count_consistency(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        assert menu.item_count() == len(menu.items)
        menu.add_item("Pancakes")
        assert menu.item_count() == len(menu.items)
        menu.add_item("Eggs")
        assert menu.item_count() == len(menu.items)

    def test_empty_string_parameters(self):
        menu = Menu("", "", "")
        assert menu.title == ""
        assert menu.description == ""
        assert menu.code == ""

    def test_add_items_preserves_order(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("First")
        menu.add_item("Second")
        menu.add_item("Third")
        assert menu.items[0] == "First"
        assert menu.items[1] == "Second"
        assert menu.items[2] == "Third"

    def test_add_item_with_special_characters(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("Eggs & Bacon")
        menu.add_item("Coffee (Hot)")
        menu.add_item("Pancakes - Blueberry")
        assert len(menu.items) == 3
        assert "Eggs & Bacon" in menu.items

    def test_add_item_with_numbers(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("2 Eggs")
        menu.add_item("3 Pancakes")
        assert len(menu.items) == 2

    def test_add_long_item_name(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        long_name = "Deluxe Continental Breakfast with Fresh Fruits and Beverages"
        menu.add_item(long_name)
        assert menu.items[0] == long_name

    def test_add_item_with_newlines_in_string(self):
        menu = Menu("Breakfast Menu", "Morning delights", "MN001")
        menu.add_item("  Item with spaces  ")
        assert "Item with spaces" in menu.items
