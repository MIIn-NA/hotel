import pytest
from reports_analytics.EmployeeReport import EmployeeReport
from user_management.Employee import Employee


class TestEmployeeReport:
    def test_init(self):
        report = EmployeeReport("2024-01-01", 10, 50)
        assert report.date == "2024-01-01"
        assert report.active_count == 10
        assert report.total == 50
        assert report.employees == []

    def test_init_with_zero_counts(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        assert report.active_count == 0
        assert report.total == 0

    def test_init_employees_list_empty(self):
        report = EmployeeReport("2024-01-01", 5, 10)
        assert isinstance(report.employees, list)
        assert len(report.employees) == 0

    def test_add_employee_valid(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp = Employee("John Doe", "Manager", "EMP001")
        report.add_employee(emp)
        assert len(report.employees) == 1
        assert report.employees[0] == emp

    def test_add_employee_increases_total(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp = Employee("Jane Smith", "Developer", "EMP002")
        report.add_employee(emp)
        assert report.total == 1

    def test_add_employee_with_long_position_increases_active(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp = Employee("Bob Johnson", "Senior Manager", "EMP003")
        report.add_employee(emp)
        assert report.active_count == 1

    def test_add_employee_with_short_position_no_active_increase(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp = Employee("Alice Brown", "PM", "EMP004")
        report.add_employee(emp)
        assert report.active_count == 0

    def test_add_employee_with_empty_position(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp = Employee("Charlie Davis", "", "EMP005")
        report.add_employee(emp)
        assert report.active_count == 0
        assert report.total == 1

    def test_add_employee_with_none_position(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp = Employee("David Wilson", "Dev", "EMP006")
        emp.position = None
        report.add_employee(emp)
        assert report.active_count == 0

    def test_add_employee_invalid_type(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        with pytest.raises(ValueError, match="Invalid Employee"):
            report.add_employee("not an employee")

    def test_add_employee_invalid_type_dict(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        with pytest.raises(ValueError, match="Invalid Employee"):
            report.add_employee({"name": "Test"})

    def test_add_employee_invalid_type_none(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        with pytest.raises(ValueError, match="Invalid Employee"):
            report.add_employee(None)

    def test_add_multiple_employees(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp1 = Employee("John Doe", "Manager", "EMP001")
        emp2 = Employee("Jane Smith", "Developer", "EMP002")
        emp3 = Employee("Bob Johnson", "Analyst", "EMP003")
        report.add_employee(emp1)
        report.add_employee(emp2)
        report.add_employee(emp3)
        assert len(report.employees) == 3
        assert report.total == 3

    def test_active_ratio_with_zero_total(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        assert report.active_ratio() == 0

    def test_active_ratio_all_active(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp1 = Employee("John Doe", "Manager", "EMP001")
        emp2 = Employee("Jane Smith", "Developer", "EMP002")
        report.add_employee(emp1)
        report.add_employee(emp2)
        assert report.active_ratio() == 1.0

    def test_active_ratio_half_active(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp1 = Employee("John Doe", "Manager", "EMP001")
        emp2 = Employee("Jane Smith", "PM", "EMP002")
        report.add_employee(emp1)
        report.add_employee(emp2)
        assert report.active_ratio() == 0.5

    def test_active_ratio_none_active(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp1 = Employee("John Doe", "PM", "EMP001")
        emp2 = Employee("Jane Smith", "IT", "EMP002")
        report.add_employee(emp1)
        report.add_employee(emp2)
        assert report.active_ratio() == 0.0

    def test_active_ratio_rounding(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        emp1 = Employee("John Doe", "Manager", "EMP001")
        emp2 = Employee("Jane Smith", "PM", "EMP002")
        emp3 = Employee("Bob Johnson", "IT", "EMP003")
        report.add_employee(emp1)
        report.add_employee(emp2)
        report.add_employee(emp3)
        assert report.active_ratio() == 0.33

    def test_active_ratio_with_initial_values(self):
        report = EmployeeReport("2024-01-01", 5, 10)
        assert report.active_ratio() == 0.5

    def test_add_employee_updates_ratio(self):
        report = EmployeeReport("2024-01-01", 0, 0)
        assert report.active_ratio() == 0
        emp = Employee("John Doe", "Manager", "EMP001")
        report.add_employee(emp)
        assert report.active_ratio() == 1.0
