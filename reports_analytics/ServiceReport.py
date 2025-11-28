class ServiceReport:
    def __init__(self, name: str, usage: int, date: str):
        self.name = name
        self.usage = usage
        self.date = date

    def update_usage(self, count: int) -> None:
        if count < 0:
            return
        self.usage += count

    def details(self) -> str:
        return f"{self.name} used {self.usage} times on {self.date}"
