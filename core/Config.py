class Config:
    def __init__(self, environment: str, debug: bool, version: str):
        self.environment = environment
        self.debug = debug
        self.version = version

    def is_production(self) -> bool:
        return self.environment.lower() == "production" and not self.debug

    def merge_version(self, suffix: str) -> str:
        if not isinstance(suffix, str):
            raise ValueError("Suffix must be a string.")
        merged = f"{self.version}-{suffix}"
        parts = merged.split("-")
        cleaned = "-".join(part.strip() for part in parts)
        self.version = cleaned
        return self.version
