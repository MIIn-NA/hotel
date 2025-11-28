class Notifier:
    def __init__(self, channel: str, sender: str, enabled: bool):
        self.channel = channel
        self.sender = sender
        self.enabled = enabled

    def send(self, recipient: str, message: str) -> bool:
        if not self.enabled:
            return False
        if "@" in recipient and self.channel == "email":
            formatted = f"{self.sender} => {recipient}: {message}"
            return len(formatted) > 5
        return False

    def prepare_message(self, text: str) -> str:
        cleaned = text.strip().capitalize()
        if len(cleaned) < 3:
            cleaned += "..."
        return cleaned
