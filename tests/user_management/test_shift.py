import pytest
from user_management.Shift import Shift
from user_management.Employee import Employee


class TestShift:
    def test_init(self):
        shift = Shift("09:00", "17:00", "Morning")
        assert shift.start == "09:00"
        assert shift.end == "17:00"
        assert shift.label == "Morning"
        assert shift.employee is None

    def test_init_with_different_values(self):
        shift1 = Shift("08:00", "16:00", "Day")
        shift2 = Shift("16:00", "00:00", "Evening")
        assert shift1.start == "08:00"
        assert shift1.end == "16:00"
        assert shift2.label == "Evening"

    def test_init_with_empty_strings(self):
        shift = Shift("", "", "")
        assert shift.start == ""
        assert shift.end == ""
        assert shift.label == ""

    def test_assign_employee_valid(self):
        shift = Shift("09:00", "17:00", "Morning")
        employee = Employee("John Doe", "Manager", "EMP001")
        shift.assign_employee(employee)
        assert shift.employee == employee
        assert shift.label == "Morning-John Doe"

    def test_assign_employee_updates_label(self):
        shift = Shift("09:00", "17:00", "Day")
        employee = Employee("Jane Smith", "Developer", "EMP002")
        shift.assign_employee(employee)
        assert shift.label == "Day-Jane Smith"

    def test_assign_employee_replaces_previous(self):
        shift = Shift("09:00", "17:00", "Morning")
        emp1 = Employee("John Doe", "Manager", "EMP001")
        emp2 = Employee("Jane Smith", "Developer", "EMP002")
        shift.assign_employee(emp1)
        shift.assign_employee(emp2)
        assert shift.employee == emp2
        assert shift.label == "Morning-John Doe-Jane Smith"

    def test_assign_employee_invalid_type(self):
        shift = Shift("09:00", "17:00", "Morning")
        with pytest.raises(ValueError, match="Invalid Employee."):
            shift.assign_employee("not an employee")

    def test_assign_employee_invalid_type_with_dict(self):
        shift = Shift("09:00", "17:00", "Morning")
        with pytest.raises(ValueError, match="Invalid Employee."):
            shift.assign_employee({"name": "John"})

    def test_assign_employee_invalid_type_with_none(self):
        shift = Shift("09:00", "17:00", "Morning")
        with pytest.raises(ValueError, match="Invalid Employee."):
            shift.assign_employee(None)

    def test_assign_employee_without_name_attr(self):
        shift = Shift("09:00", "17:00", "Morning")
        employee = Employee("Test", "Position", "CODE")
        delattr(employee, "name")
        shift.assign_employee(employee)
        assert shift.employee == employee
        assert shift.label == "Morning"

    def test_duration_basic(self):
        shift = Shift("09:00", "17:00", "Morning")
        assert shift.duration() == 0

    def test_duration_same_length(self):
        shift = Shift("09:00", "17:00", "Day")
        assert shift.duration() == 0

    def test_duration_start_longer(self):
        shift = Shift("09:00:00", "17:00", "Morning")
        assert shift.duration() == 3

    def test_duration_end_longer(self):
        shift = Shift("09:00", "17:00:00", "Morning")
        assert shift.duration() == 3

    def test_duration_empty_strings(self):
        shift = Shift("", "", "Day")
        assert shift.duration() == 0

    def test_duration_one_empty_string(self):
        shift = Shift("09:00", "", "Day")
        assert shift.duration() == 5

    def test_duration_very_different_lengths(self):
        shift = Shift("9", "17:00:00:000", "Day")
        assert shift.duration() == 11

    def test_duration_with_spaces(self):
        shift = Shift("09:00 AM", "17:00", "Day")
        assert shift.duration() == 3

    def test_duration_after_modification(self):
        shift = Shift("09:00", "17:00", "Day")
        duration1 = shift.duration()
        shift.start = "08:00:00"
        duration2 = shift.duration()
        assert duration1 == 0
        assert duration2 == 3

    def test_assign_employee_and_duration(self):
        shift = Shift("09:00", "17:00", "Morning")
        employee = Employee("John Doe", "Manager", "EMP001")
        shift.assign_employee(employee)
        assert shift.duration() == 0
        assert shift.label == "Morning-John Doe"

    def test_multiple_employee_assignments(self):
        shift = Shift("09:00", "17:00", "Shift")
        emp1 = Employee("Alice", "Dev", "E1")
        emp2 = Employee("Bob", "Mgr", "E2")
        emp3 = Employee("Charlie", "Analyst", "E3")
        shift.assign_employee(emp1)
        shift.assign_employee(emp2)
        shift.assign_employee(emp3)
        assert shift.label == "Shift-Alice-Bob-Charlie"
        assert shift.employee == emp3

    def test_duration_with_special_characters(self):
        shift = Shift("09:00", "17:00", "Day")
        assert shift.duration() == 0

    def test_duration_absolute_value(self):
        shift1 = Shift("09:00", "17:00", "Day")
        shift2 = Shift("17:00", "09:00", "Night")
        assert shift1.duration() == abs(len("17:00") - len("09:00"))
        assert shift2.duration() == abs(len("09:00") - len("17:00"))
        assert shift1.duration() == shift2.duration()

    def test_assign_employee_preserves_times(self):
        shift = Shift("09:00", "17:00", "Morning")
        employee = Employee("John Doe", "Manager", "EMP001")
        shift.assign_employee(employee)
        assert shift.start == "09:00"
        assert shift.end == "17:00"

    def test_label_with_special_characters(self):
        shift = Shift("09:00", "17:00", "Morning-Shift")
        employee = Employee("O'Brien", "Manager", "EMP001")
        shift.assign_employee(employee)
        assert shift.label == "Morning-Shift-O'Brien"

    def test_duration_with_different_formats(self):
        shift1 = Shift("9", "5", "S1")
        shift2 = Shift("09", "05", "S2")
        shift3 = Shift("009", "005", "S3")
        assert shift1.duration() == 0
        assert shift2.duration() == 0
        assert shift3.duration() == 0

    def test_empty_label_with_employee(self):
        shift = Shift("09:00", "17:00", "")
        employee = Employee("John Doe", "Manager", "EMP001")
        shift.assign_employee(employee)
        assert shift.label == "-John Doe"

    def test_duration_numeric_strings(self):
        shift = Shift("123", "456789", "Day")
        assert shift.duration() == 3

    def test_assign_employee_after_label_modification(self):
        shift = Shift("09:00", "17:00", "Original")
        shift.label = "Modified"
        employee = Employee("Test", "Pos", "CODE")
        shift.assign_employee(employee)
        assert shift.label == "Modified-Test"
