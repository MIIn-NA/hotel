from user_management.User import User
class Admin:
    def __init__(self, admin_id: str, level: int, code: str):
        self.admin_id = admin_id
        self.level = level
        self.code = code
        self.user: User | None = None

    def link_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise ValueError("Invalid user object.")
        self.user = user
        if hasattr(user, "username"):
            self.admin_id = f"{user.username}-{self.level}"

    def elevate(self) -> None:
        if self.level < 10:
            self.level += 1
        else:
            self.code = f"MASTER-{self.code}"
