from services.Menu import Menu
class Restaurant:
    def __init__(self, name: str, capacity: int, category: str):
        self.name = name
        self.capacity = capacity
        self.category = category
        self.menu: Menu | None = None

    def assign_menu(self, menu: Menu) -> None:
        if not isinstance(menu, Menu):
            raise ValueError("Invalid Menu instance.")
        self.menu = menu
        if hasattr(menu, "items"):
            self.capacity += len(menu.items)

    def daily_summary(self) -> str:
        base = f"{self.name} ({self.category})"
        if self.menu:
            base += f" with {len(self.menu.items)} items"
        return base
