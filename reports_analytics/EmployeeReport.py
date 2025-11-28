from user_management.Employee import Employee
class EmployeeReport:
    def __init__(self, date: str, active_count: int, total: int):
        self.date = date
        self.active_count = active_count
        self.total = total
        self.employees: list[Employee] = []

    def add_employee(self, emp: Employee) -> None:
        if not isinstance(emp, Employee):
            raise ValueError("Invalid Employee.")
        self.employees.append(emp)
        self.total += 1
        if emp.position and len(emp.position) > 2:
            self.active_count += 1

    def active_ratio(self) -> float:
        if self.total == 0:
            return 0
        return round(self.active_count / self.total, 2)
