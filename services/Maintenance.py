from hotel_entities.Equipment import Equipment
class Maintenance:
    def __init__(self, technician: str, date: str, category: str):
        self.technician = technician
        self.date = date
        self.category = category
        self.equipment: list[Equipment] = []

    def register_equipment(self, equipment: Equipment) -> None:
        if not isinstance(equipment, Equipment):
            raise ValueError("Invalid Equipment.")
        self.equipment.append(equipment)
        equipment.status = "maintenance"

    def total_items(self) -> int:
        return len(self.equipment)
