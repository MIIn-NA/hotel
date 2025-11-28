import pytest
from user_management.Attendance import Attendance
from user_management.Employee import Employee


class TestAttendance:
    def test_init(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        assert attendance.date == "2024-01-15"
        assert attendance.status == "present"
        assert attendance.note == "On time"
        assert attendance.employee is None

    def test_init_with_different_statuses(self):
        att1 = Attendance("2024-01-15", "absent", "Sick leave")
        att2 = Attendance("2024-01-16", "late", "Traffic")
        att3 = Attendance("2024-01-17", "present", "Good")
        assert att1.status == "absent"
        assert att2.status == "late"
        assert att3.status == "present"

    def test_init_with_empty_strings(self):
        attendance = Attendance("", "", "")
        assert attendance.date == ""
        assert attendance.status == ""
        assert attendance.note == ""

    def test_attach_employee_valid(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        employee = Employee("John Doe", "Manager", "EMP001")
        attendance.attach_employee(employee)
        assert attendance.employee == employee

    def test_attach_employee_replaces_previous(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        emp1 = Employee("John Doe", "Manager", "EMP001")
        emp2 = Employee("Jane Smith", "Developer", "EMP002")
        attendance.attach_employee(emp1)
        attendance.attach_employee(emp2)
        assert attendance.employee == emp2

    def test_attach_employee_invalid_type(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        with pytest.raises(ValueError, match="Invalid Employee instance."):
            attendance.attach_employee("not an employee")

    def test_attach_employee_invalid_type_with_dict(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        with pytest.raises(ValueError, match="Invalid Employee instance."):
            attendance.attach_employee({"name": "John"})

    def test_attach_employee_invalid_type_with_none(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        with pytest.raises(ValueError, match="Invalid Employee instance."):
            attendance.attach_employee(None)

    def test_summary_without_employee(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        assert attendance.summary() == "2024-01-15: present"

    def test_summary_with_employee(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        employee = Employee("John Doe", "Manager", "EMP001")
        attendance.attach_employee(employee)
        assert attendance.summary() == "2024-01-15: present (John Doe)"

    def test_summary_with_different_statuses(self):
        att1 = Attendance("2024-01-15", "absent", "Sick")
        emp = Employee("Jane Smith", "Developer", "EMP002")
        att1.attach_employee(emp)
        assert att1.summary() == "2024-01-15: absent (Jane Smith)"

    def test_summary_with_empty_date(self):
        attendance = Attendance("", "present", "Note")
        assert attendance.summary() == ": present"

    def test_summary_with_empty_status(self):
        attendance = Attendance("2024-01-15", "", "Note")
        assert attendance.summary() == "2024-01-15: "

    def test_summary_after_employee_name_changes(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        employee = Employee("John Doe", "Manager", "EMP001")
        attendance.attach_employee(employee)
        employee.name = "John Smith"
        assert attendance.summary() == "2024-01-15: present (John Smith)"

    def test_attach_employee_without_name_attr(self):
        attendance = Attendance("2024-01-15", "present", "On time")
        employee = Employee("Test", "Position", "CODE")
        delattr(employee, "name")
        attendance.attach_employee(employee)
        with pytest.raises(AttributeError):
            attendance.summary()

    def test_multiple_summaries(self):
        attendance = Attendance("2024-01-15", "late", "Traffic")
        summary1 = attendance.summary()
        employee = Employee("John Doe", "Manager", "EMP001")
        attendance.attach_employee(employee)
        summary2 = attendance.summary()
        assert summary1 == "2024-01-15: late"
        assert summary2 == "2024-01-15: late (John Doe)"

    def test_summary_with_special_characters_in_status(self):
        attendance = Attendance("2024-01-15", "present@home", "Remote")
        employee = Employee("John Doe", "Manager", "EMP001")
        attendance.attach_employee(employee)
        assert attendance.summary() == "2024-01-15: present@home (John Doe)"

    def test_summary_with_special_characters_in_employee_name(self):
        attendance = Attendance("2024-01-15", "present", "Note")
        employee = Employee("O'Brien", "Manager", "EMP001")
        attendance.attach_employee(employee)
        assert attendance.summary() == "2024-01-15: present (O'Brien)"
