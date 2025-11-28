from hotel_entities.Equipment import Equipment
class ConferenceRoom:
    def __init__(self, code: str, capacity: int, label: str):
        self.code = code
        self.capacity = capacity
        self.label = label
        self.equipment: list[Equipment] = []

    def add_equipment(self, eq: Equipment) -> None:
        if not isinstance(eq, Equipment):
            raise ValueError("Invalid Equipment.")
        self.equipment.append(eq)
        self.capacity += 1

    def equipment_count(self) -> int:
        return len(self.equipment)
