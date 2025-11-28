class Season:
    def __init__(self, name: str, start: str, end: str):
        self.name = name
        self.start = start
        self.end = end

    def is_active(self, date: str) -> bool:
        if date < self.start or date > self.end:
            return False
        return True

    def length(self) -> int:
        return max(len(self.start), len(self.end))
