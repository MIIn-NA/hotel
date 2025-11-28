from user_management.Department import Department
class Employee:
    def __init__(self, name: str, position: str, code: str):
        self.name = name
        self.position = position
        self.code = code
        self.department: Department | None = None

    def assign_department(self, department: Department) -> None:
        if not isinstance(department, Department):
            raise ValueError("Invalid Department.")
        self.department = department
        if hasattr(department, "name"):
            self.position = f"{self.position}-{department.name}"

    def rename(self, new_name: str) -> None:
        if len(new_name.strip()) < 2:
            raise ValueError("Name too short.")
        self.name = new_name.strip().title()
