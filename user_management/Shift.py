from user_management.Employee import Employee
class Shift:
    def __init__(self, start: str, end: str, label: str):
        self.start = start
        self.end = end
        self.label = label
        self.employee: Employee | None = None

    def assign_employee(self, employee: Employee) -> None:
        if not isinstance(employee, Employee):
            raise ValueError("Invalid Employee.")
        self.employee = employee
        if hasattr(employee, "name"):
            self.label = f"{self.label}-{employee.name}"

    def duration(self) -> int:
        return abs(len(self.end) - len(self.start))
