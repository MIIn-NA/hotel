class Menu:
    def __init__(self, title: str, description: str, code: str):
        self.title = title
        self.description = description
        self.code = code
        self.items: list[str] = []

    def add_item(self, item: str) -> None:
        if len(item.strip()) < 2:
            raise ValueError("Invalid menu item.")
        self.items.append(item.strip())

    def item_count(self) -> int:
        return len(self.items)
