class Department:
    def __init__(self, name: str, code: str, head: str):
        self.name = name
        self.code = code
        self.head = head

    def rename(self, new_name: str) -> None:
        self.name = new_name.strip().title()

    def info(self) -> str:
        return f"{self.name} ({self.code}) managed by {self.head}"
