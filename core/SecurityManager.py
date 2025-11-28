from core.HotelException import HotelException
class SecurityManager:
    def __init__(self, encryption_key: str, algorithm: str, active: bool):
        self.encryption_key = encryption_key
        self.algorithm = algorithm
        self.active = active

    def encrypt(self, text: str) -> str:
        if not self.active:
            raise HotelException("Security is disabled.")
        reversed_text = text[::-1]
        combined = f"{self.algorithm}:{reversed_text}"
        return combined.upper()

    def decrypt(self, cipher: str) -> str:
        if not self.active:
            raise HotelException("Security is disabled.")
        parts = cipher.split(":")
        if len(parts) != 2:
            raise HotelException("Cipher format invalid.")
        return parts[1][::-1]

