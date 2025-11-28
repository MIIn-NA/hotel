import pytest
from services.Restaurant import Restaurant
from services.Menu import Menu


class TestRestaurant:
    def test_init(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        assert restaurant.name == "The Grand Dining"
        assert restaurant.capacity == 100
        assert restaurant.category == "Fine Dining"
        assert restaurant.menu is None

    def test_init_with_different_values(self):
        restaurant = Restaurant("Cafe Corner", 50, "Casual")
        assert restaurant.name == "Cafe Corner"
        assert restaurant.capacity == 50
        assert restaurant.category == "Casual"

    def test_init_with_zero_capacity(self):
        restaurant = Restaurant("Private Room", 0, "Exclusive")
        assert restaurant.capacity == 0
        assert restaurant.menu is None

    def test_assign_menu_valid(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        restaurant.assign_menu(menu)
        assert restaurant.menu == menu

    def test_assign_menu_increases_capacity(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        menu.add_item("Steak")
        menu.add_item("Salmon")
        menu.add_item("Pasta")
        initial_capacity = restaurant.capacity
        restaurant.assign_menu(menu)
        assert restaurant.capacity == initial_capacity + 3

    def test_assign_menu_empty_items(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        restaurant.assign_menu(menu)
        assert restaurant.capacity == 100

    def test_assign_menu_with_single_item(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        menu.add_item("Steak")
        restaurant.assign_menu(menu)
        assert restaurant.capacity == 101

    def test_assign_menu_invalid_type(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        with pytest.raises(ValueError, match="Invalid Menu instance."):
            restaurant.assign_menu("not a menu")

    def test_assign_menu_none(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        with pytest.raises(ValueError, match="Invalid Menu instance."):
            restaurant.assign_menu(None)

    def test_assign_menu_invalid_object(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        with pytest.raises(ValueError, match="Invalid Menu instance."):
            restaurant.assign_menu({"title": "Menu"})

    def test_assign_menu_multiple_times(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu1 = Menu("Breakfast Menu", "Morning specials", "MN001")
        menu1.add_item("Eggs")
        menu1.add_item("Bacon")
        menu2 = Menu("Dinner Menu", "Evening specials", "MN002")
        menu2.add_item("Steak")
        menu2.add_item("Wine")
        menu2.add_item("Dessert")

        restaurant.assign_menu(menu1)
        assert restaurant.capacity == 102
        restaurant.assign_menu(menu2)
        assert restaurant.menu == menu2
        assert restaurant.capacity == 105

    def test_assign_menu_with_many_items(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Full Menu", "Complete offerings", "MN001")
        for i in range(10):
            menu.add_item(f"Item {i}")
        restaurant.assign_menu(menu)
        assert restaurant.capacity == 110

    def test_daily_summary_without_menu(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        summary = restaurant.daily_summary()
        assert summary == "The Grand Dining (Fine Dining)"
        assert "with" not in summary

    def test_daily_summary_with_menu_no_items(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        restaurant.assign_menu(menu)
        summary = restaurant.daily_summary()
        assert summary == "The Grand Dining (Fine Dining) with 0 items"

    def test_daily_summary_with_menu_single_item(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        menu.add_item("Steak")
        restaurant.assign_menu(menu)
        summary = restaurant.daily_summary()
        assert summary == "The Grand Dining (Fine Dining) with 1 items"

    def test_daily_summary_with_menu_multiple_items(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        menu.add_item("Steak")
        menu.add_item("Salmon")
        menu.add_item("Pasta")
        restaurant.assign_menu(menu)
        summary = restaurant.daily_summary()
        assert summary == "The Grand Dining (Fine Dining) with 3 items"

    def test_daily_summary_format_without_menu(self):
        restaurant = Restaurant("Cafe Corner", 50, "Casual")
        summary = restaurant.daily_summary()
        assert restaurant.name in summary
        assert restaurant.category in summary
        assert "(" in summary and ")" in summary

    def test_daily_summary_format_with_menu(self):
        restaurant = Restaurant("Cafe Corner", 50, "Casual")
        menu = Menu("Lunch Menu", "Midday options", "MN001")
        menu.add_item("Sandwich")
        menu.add_item("Salad")
        restaurant.assign_menu(menu)
        summary = restaurant.daily_summary()
        assert "Cafe Corner" in summary
        assert "Casual" in summary
        assert "2 items" in summary

    def test_empty_string_parameters(self):
        restaurant = Restaurant("", 0, "")
        assert restaurant.name == ""
        assert restaurant.capacity == 0
        assert restaurant.category == ""

    def test_negative_capacity(self):
        restaurant = Restaurant("Restaurant", -10, "Category")
        assert restaurant.capacity == -10
        menu = Menu("Menu", "Description", "MN001")
        menu.add_item("Item1")
        menu.add_item("Item2")
        restaurant.assign_menu(menu)
        assert restaurant.capacity == -8

    def test_assign_menu_capacity_calculation(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        items = ["Appetizer", "Main Course", "Dessert", "Beverage", "Special"]
        for item in items:
            menu.add_item(item)
        initial = restaurant.capacity
        restaurant.assign_menu(menu)
        assert restaurant.capacity == initial + len(items)

    def test_menu_without_items_attribute(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        assert hasattr(menu, "items")
        restaurant.assign_menu(menu)
        assert restaurant.capacity == 100

    def test_assign_menu_preserves_menu_reference(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        menu.add_item("Steak")
        restaurant.assign_menu(menu)
        assert restaurant.menu is menu
        menu.add_item("Wine")
        assert len(restaurant.menu.items) == 2

    def test_daily_summary_after_menu_modification(self):
        restaurant = Restaurant("The Grand Dining", 100, "Fine Dining")
        menu = Menu("Dinner Menu", "Evening specials", "MN001")
        menu.add_item("Steak")
        restaurant.assign_menu(menu)
        summary1 = restaurant.daily_summary()
        assert "1 items" in summary1
        menu.add_item("Wine")
        summary2 = restaurant.daily_summary()
        assert "2 items" in summary2
