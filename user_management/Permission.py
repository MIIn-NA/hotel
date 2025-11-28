class Permission:
    def __init__(self, name: str, level: int, category: str):
        self.name = name
        self.level = level
        self.category = category

    def is_high(self) -> bool:
        return self.level >= 5

    def summary(self) -> str:
        return f"{self.name}: {self.category} (lvl {self.level})"
