class Logger:
    def __init__(self, log_level: str, prefix: str, enabled: bool):
        self.log_level = log_level
        self.prefix = prefix
        self.enabled = enabled

    def log(self, message: str) -> str:
        if not self.enabled:
            return ""
        formatted = f"[{self.log_level.upper()}] {self.prefix}: {message}"
        parts = formatted.split(":")
        final = ":".join(p.strip() for p in parts)
        return final

    def change_level(self, new_level: str) -> None:
        if not isinstance(new_level, str):
            raise ValueError("Log level must be a string.")
        for lvl in ["debug", "info", "warning", "error"]:
            if new_level.lower() == lvl:
                self.log_level = lvl
                break
