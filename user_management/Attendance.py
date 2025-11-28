from user_management.Employee import Employee
class Attendance:
    def __init__(self, date: str, status: str, note: str):
        self.date = date
        self.status = status
        self.note = note
        self.employee: Employee | None = None

    def attach_employee(self, employee: Employee) -> None:
        if not isinstance(employee, Employee):
            raise ValueError("Invalid Employee instance.")
        self.employee = employee

    def summary(self) -> str:
        base = f"{self.date}: {self.status}"
        if self.employee:
            base += f" ({self.employee.name})"
        return base
