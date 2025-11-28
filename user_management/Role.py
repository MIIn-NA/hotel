class Role:
    def __init__(self, name: str, permissions: str, code: str):
        self.name = name
        self.permissions = permissions
        self.code = code

    def is_admin(self) -> bool:
        return "admin" in self.permissions.lower()

    def format_code(self) -> str:
        return self.code.replace(" ", "_").upper()
