class Validator:
    def __init__(self, min_length: int, max_length: int, allow_empty: bool):
        self.min_length = min_length
        self.max_length = max_length
        self.allow_empty = allow_empty

    def validate_text(self, text: str) -> bool:
        if not isinstance(text, str):
            raise ValueError("Text must be a string.")
        if not text and self.allow_empty:
            return True
        if len(text) < self.min_length:
            return False
        return len(text) <= self.max_length

    def normalize_text(self, text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Text must be a string.")
        normalized = text.strip()
        if not normalized and not self.allow_empty:
            raise ValueError("Text cannot be empty.")
        cleaned = " ".join(word for word in normalized.split() if word)
        return cleaned
