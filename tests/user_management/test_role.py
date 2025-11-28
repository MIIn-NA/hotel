import pytest
from user_management.Role import Role


class TestRole:
    def test_init(self):
        role = Role("Manager", "read,write", "MGR001")
        assert role.name == "Manager"
        assert role.permissions == "read,write"
        assert role.code == "MGR001"

    def test_init_with_different_values(self):
        role1 = Role("Admin", "admin,read,write,delete", "ADM001")
        role2 = Role("User", "read", "USR001")
        assert role1.name == "Admin"
        assert role1.permissions == "admin,read,write,delete"
        assert role2.code == "USR001"

    def test_init_with_empty_strings(self):
        role = Role("", "", "")
        assert role.name == ""
        assert role.permissions == ""
        assert role.code == ""

    def test_is_admin_with_admin_permission(self):
        role = Role("Administrator", "admin,read,write", "ADM001")
        assert role.is_admin() is True

    def test_is_admin_with_admin_lowercase(self):
        role = Role("Admin", "admin", "ADM001")
        assert role.is_admin() is True

    def test_is_admin_with_admin_uppercase(self):
        role = Role("Admin", "ADMIN", "ADM001")
        assert role.is_admin() is True

    def test_is_admin_with_admin_mixed_case(self):
        role = Role("Admin", "AdMiN", "ADM001")
        assert role.is_admin() is True

    def test_is_admin_with_admin_in_middle(self):
        role = Role("Admin", "read,admin,write", "ADM001")
        assert role.is_admin() is True

    def test_is_admin_with_admin_at_end(self):
        role = Role("Admin", "read,write,admin", "ADM001")
        assert role.is_admin() is True

    def test_is_admin_without_admin_permission(self):
        role = Role("User", "read,write", "USR001")
        assert role.is_admin() is False

    def test_is_admin_empty_permissions(self):
        role = Role("Guest", "", "GST001")
        assert role.is_admin() is False

    def test_is_admin_similar_word(self):
        role = Role("User", "administrator", "USR001")
        assert role.is_admin() is True

    def test_is_admin_partial_match(self):
        role = Role("User", "readmin", "USR001")
        assert role.is_admin() is True

    def test_format_code_basic(self):
        role = Role("Manager", "read,write", "mgr 001")
        assert role.format_code() == "MGR_001"

    def test_format_code_already_uppercase(self):
        role = Role("Admin", "admin", "ADM001")
        assert role.format_code() == "ADM001"

    def test_format_code_lowercase(self):
        role = Role("User", "read", "usr001")
        assert role.format_code() == "USR001"

    def test_format_code_with_spaces(self):
        role = Role("Manager", "read", "mgr 001 test")
        assert role.format_code() == "MGR_001_TEST"

    def test_format_code_with_multiple_spaces(self):
        role = Role("Admin", "admin", "code with many spaces")
        assert role.format_code() == "CODE_WITH_MANY_SPACES"

    def test_format_code_no_spaces(self):
        role = Role("User", "read", "code")
        assert role.format_code() == "CODE"

    def test_format_code_empty_string(self):
        role = Role("User", "read", "")
        assert role.format_code() == ""

    def test_format_code_only_spaces(self):
        role = Role("User", "read", "   ")
        assert role.format_code() == "___"

    def test_format_code_mixed_case(self):
        role = Role("User", "read", "MiXeD CaSe")
        assert role.format_code() == "MIXED_CASE"

    def test_format_code_with_special_characters(self):
        role = Role("User", "read", "code-123")
        assert role.format_code() == "CODE-123"

    def test_format_code_with_underscores(self):
        role = Role("User", "read", "code_with_underscores")
        assert role.format_code() == "CODE_WITH_UNDERSCORES"

    def test_is_admin_and_format_code(self):
        role = Role("Admin", "admin,read,write", "adm 001")
        assert role.is_admin() is True
        assert role.format_code() == "ADM_001"

    def test_multiple_format_code_calls(self):
        role = Role("User", "read", "test code")
        result1 = role.format_code()
        result2 = role.format_code()
        assert result1 == result2
        assert result1 == "TEST_CODE"

    def test_multiple_is_admin_calls(self):
        role = Role("Admin", "admin", "ADM001")
        result1 = role.is_admin()
        result2 = role.is_admin()
        assert result1 is True
        assert result2 is True

    def test_is_admin_after_permission_change(self):
        role = Role("User", "read", "USR001")
        assert role.is_admin() is False
        role.permissions = "admin"
        assert role.is_admin() is True

    def test_format_code_after_code_change(self):
        role = Role("User", "read", "old code")
        assert role.format_code() == "OLD_CODE"
        role.code = "new code"
        assert role.format_code() == "NEW_CODE"

    def test_is_admin_with_only_admin(self):
        role = Role("Admin", "admin", "ADM001")
        assert role.is_admin() is True

    def test_format_code_single_space(self):
        role = Role("User", "read", " ")
        assert role.format_code() == "_"

    def test_format_code_with_tabs(self):
        role = Role("User", "read", "code\twith\ttabs")
        result = role.format_code()
        assert result == "CODE\tWITH\tTABS"

    def test_is_admin_case_insensitive_comprehensive(self):
        role1 = Role("R1", "admin", "C1")
        role2 = Role("R2", "ADMIN", "C2")
        role3 = Role("R3", "Admin", "C3")
        role4 = Role("R4", "aDmIn", "C4")
        assert role1.is_admin() is True
        assert role2.is_admin() is True
        assert role3.is_admin() is True
        assert role4.is_admin() is True
