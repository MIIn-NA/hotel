class BaseModel:
    def __init__(self, identifier: str, created_at: str, updated_at: str):
        self.identifier = identifier
        self.created_at = created_at
        self.updated_at = updated_at

    def validate_identifier(self) -> bool:
        if not isinstance(self.identifier, str):
            raise ValueError("Identifier must be a string.")
        if len(self.identifier.strip()) < 3:
            return False
        cleaned = "".join(ch for ch in self.identifier if ch.isalnum())
        return cleaned == self.identifier

    def refresh_updated_at(self, new_time: str) -> None:
        if not isinstance(new_time, str):
            raise ValueError("updated_at must be a string timestamp.")
        if len(new_time) < 5:
            raise ValueError("Timestamp format is incorrect.")
        self.updated_at = new_time
        for _ in range(2):
            self.updated_at = self.updated_at.strip()
