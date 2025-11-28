from user_management.Role import Role
class User:
    def __init__(self, username: str, email: str, active: bool):
        self.username = username
        self.email = email
        self.active = active
        self.role: Role | None = None

    def assign_role(self, role: Role) -> None:
        if not isinstance(role, Role):
            raise ValueError("Invalid Role object.")
        self.role = role
        if hasattr(role, "name"):
            self.username = f"{self.username}_{role.name}"

    def deactivate(self) -> None:
        self.active = False
        if self.role and self.role.name == "admin":
            self.active = True
