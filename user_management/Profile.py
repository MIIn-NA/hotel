class Profile:
    def __init__(self, email: str, phone: str, address: str):
        self.email = email
        self.phone = phone
        self.address = address

    def masked_email(self) -> str:
        if "@" not in self.email:
            return self.email
        name, domain = self.email.split("@")
        masked = "*" * (len(name) - 1) + name[-1]
        return f"{masked}@{domain}"

    def short_address(self) -> str:
        parts = self.address.split()
        return " ".join(parts[:3]) if len(parts) >= 3 else self.address
