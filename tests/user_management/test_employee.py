import pytest
from user_management.Employee import Employee
from user_management.Department import Department


class TestEmployee:
    def test_init(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        assert emp.name == "John Doe"
        assert emp.position == "Manager"
        assert emp.code == "EMP001"
        assert emp.department is None

    def test_init_with_different_values(self):
        emp1 = Employee("Jane Smith", "Developer", "DEV001")
        emp2 = Employee("Bob Johnson", "Analyst", "ANA001")
        assert emp1.name == "Jane Smith"
        assert emp1.position == "Developer"
        assert emp2.name == "Bob Johnson"
        assert emp2.code == "ANA001"

    def test_init_with_empty_strings(self):
        emp = Employee("", "", "")
        assert emp.name == ""
        assert emp.position == ""
        assert emp.code == ""

    def test_assign_department_valid(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        dept = Department("Engineering", "ENG", "Jane Smith")
        emp.assign_department(dept)
        assert emp.department == dept
        assert emp.position == "Manager-Engineering"

    def test_assign_department_updates_position(self):
        emp = Employee("John Doe", "Developer", "EMP001")
        dept = Department("Sales", "SAL", "Boss")
        emp.assign_department(dept)
        assert emp.position == "Developer-Sales"

    def test_assign_department_replaces_previous(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        dept1 = Department("Engineering", "ENG", "Jane")
        dept2 = Department("Sales", "SAL", "Bob")
        emp.assign_department(dept1)
        emp.assign_department(dept2)
        assert emp.department == dept2
        assert emp.position == "Manager-Engineering-Sales"

    def test_assign_department_invalid_type(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        with pytest.raises(ValueError, match="Invalid Department."):
            emp.assign_department("not a department")

    def test_assign_department_invalid_type_with_dict(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        with pytest.raises(ValueError, match="Invalid Department."):
            emp.assign_department({"name": "Engineering"})

    def test_assign_department_invalid_type_with_none(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        with pytest.raises(ValueError, match="Invalid Department."):
            emp.assign_department(None)

    def test_assign_department_without_name_attr(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        dept = Department("Engineering", "ENG", "Jane")
        delattr(dept, "name")
        emp.assign_department(dept)
        assert emp.department == dept
        assert emp.position == "Manager"

    def test_rename_basic(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("jane smith")
        assert emp.name == "Jane Smith"

    def test_rename_title_case(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("bob johnson")
        assert emp.name == "Bob Johnson"

    def test_rename_all_caps(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("ALICE WONG")
        assert emp.name == "Alice Wong"

    def test_rename_with_whitespace(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("  jane smith  ")
        assert emp.name == "Jane Smith"

    def test_rename_too_short(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        with pytest.raises(ValueError, match="Name too short."):
            emp.rename("A")

    def test_rename_single_character_with_whitespace(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        with pytest.raises(ValueError, match="Name too short."):
            emp.rename(" X ")

    def test_rename_empty_string(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        with pytest.raises(ValueError, match="Name too short."):
            emp.rename("")

    def test_rename_only_whitespace(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        with pytest.raises(ValueError, match="Name too short."):
            emp.rename("   ")

    def test_rename_exactly_two_characters(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("AB")
        assert emp.name == "Ab"

    def test_rename_two_characters_with_whitespace(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("  XY  ")
        assert emp.name == "Xy"

    def test_rename_multiple_times(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("Alice")
        assert emp.name == "Alice"
        emp.rename("Bob")
        assert emp.name == "Bob"
        emp.rename("Charlie Brown")
        assert emp.name == "Charlie Brown"

    def test_rename_preserves_position_and_code(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("Jane Smith")
        assert emp.position == "Manager"
        assert emp.code == "EMP001"

    def test_rename_with_special_characters(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("o'brien")
        assert emp.name == "O'Brien"

    def test_rename_mixed_case(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("jOhN sMiTh")
        assert emp.name == "John Smith"

    def test_assign_department_and_rename(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        dept = Department("Engineering", "ENG", "Jane")
        emp.assign_department(dept)
        emp.rename("Bob Smith")
        assert emp.name == "Bob Smith"
        assert emp.position == "Manager-Engineering"
        assert emp.department == dept

    def test_rename_and_assign_department(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("Alice Wong")
        dept = Department("Sales", "SAL", "Boss")
        emp.assign_department(dept)
        assert emp.name == "Alice Wong"
        assert emp.position == "Manager-Sales"

    def test_multiple_department_assignments(self):
        emp = Employee("John Doe", "Dev", "EMP001")
        dept1 = Department("Eng", "E1", "H1")
        dept2 = Department("Sales", "S1", "H2")
        dept3 = Department("HR", "H1", "H3")
        emp.assign_department(dept1)
        emp.assign_department(dept2)
        emp.assign_department(dept3)
        assert emp.position == "Dev-Eng-Sales-HR"

    def test_rename_with_numbers(self):
        emp = Employee("John Doe", "Manager", "EMP001")
        emp.rename("employee 42")
        assert emp.name == "Employee 42"
