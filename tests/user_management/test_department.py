import pytest
from user_management.Department import Department


class TestDepartment:
    def test_init(self):
        dept = Department("Engineering", "ENG", "John Doe")
        assert dept.name == "Engineering"
        assert dept.code == "ENG"
        assert dept.head == "John Doe"

    def test_init_with_different_values(self):
        dept1 = Department("Sales", "SAL", "Jane Smith")
        dept2 = Department("HR", "HR001", "Bob Johnson")
        assert dept1.name == "Sales"
        assert dept1.code == "SAL"
        assert dept2.name == "HR"
        assert dept2.head == "Bob Johnson"

    def test_init_with_empty_strings(self):
        dept = Department("", "", "")
        assert dept.name == ""
        assert dept.code == ""
        assert dept.head == ""

    def test_rename_basic(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("marketing")
        assert dept.name == "Marketing"

    def test_rename_title_case(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("human resources")
        assert dept.name == "Human Resources"

    def test_rename_all_caps(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("SALES")
        assert dept.name == "Sales"

    def test_rename_with_whitespace(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("  marketing  ")
        assert dept.name == "Marketing"

    def test_rename_multiple_times(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("Sales")
        assert dept.name == "Sales"
        dept.rename("HR")
        assert dept.name == "Hr"
        dept.rename("finance")
        assert dept.name == "Finance"

    def test_rename_with_multiple_words(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("customer support team")
        assert dept.name == "Customer Support Team"

    def test_rename_empty_string(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("")
        assert dept.name == ""

    def test_rename_only_whitespace(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("   ")
        assert dept.name == ""

    def test_rename_mixed_case(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("SaLeS aNd MaRkEtInG")
        assert dept.name == "Sales And Marketing"

    def test_info_basic(self):
        dept = Department("Engineering", "ENG", "John Doe")
        assert dept.info() == "Engineering (ENG) managed by John Doe"

    def test_info_after_rename(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("Sales")
        assert dept.info() == "Sales (ENG) managed by John Doe"

    def test_info_with_empty_values(self):
        dept = Department("", "", "")
        assert dept.info() == " () managed by "

    def test_info_with_special_characters(self):
        dept = Department("R&D", "RND-001", "O'Brien")
        assert dept.info() == "R&D (RND-001) managed by O'Brien"

    def test_rename_preserves_code_and_head(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("Sales")
        assert dept.code == "ENG"
        assert dept.head == "John Doe"

    def test_multiple_operations(self):
        dept = Department("Engineering", "ENG", "John Doe")
        info1 = dept.info()
        dept.rename("Sales")
        info2 = dept.info()
        dept.rename("marketing")
        info3 = dept.info()
        assert info1 == "Engineering (ENG) managed by John Doe"
        assert info2 == "Sales (ENG) managed by John Doe"
        assert info3 == "Marketing (ENG) managed by John Doe"

    def test_rename_with_numbers(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("department 42")
        assert dept.name == "Department 42"

    def test_rename_single_character(self):
        dept = Department("Engineering", "ENG", "John Doe")
        dept.rename("x")
        assert dept.name == "X"

    def test_info_format_consistency(self):
        dept = Department("Sales", "SAL", "Jane")
        info = dept.info()
        assert "Sales" in info
        assert "SAL" in info
        assert "Jane" in info
        assert info.count("(") == 1
        assert info.count(")") == 1
