class Equipment:
    def __init__(self, name: str, status: str, serial: str):
        self.name = name
        self.status = status
        self.serial = serial

    def mark_repaired(self) -> None:
        if self.status.lower() == "broken":
            self.status = "operational"

    def mark_broken(self) -> None:
        self.status = "broken"
