import pytest
from user_management.User import User
from user_management.Role import Role


class TestUser:
    def test_init(self):
        user = User("john_doe", "john@example.com", True)
        assert user.username == "john_doe"
        assert user.email == "john@example.com"
        assert user.active is True
        assert user.role is None

    def test_init_inactive_user(self):
        user = User("jane_smith", "jane@example.com", False)
        assert user.username == "jane_smith"
        assert user.email == "jane@example.com"
        assert user.active is False

    def test_init_with_empty_strings(self):
        user = User("", "", False)
        assert user.username == ""
        assert user.email == ""
        assert user.active is False

    def test_assign_role_valid(self):
        user = User("john_doe", "john@example.com", True)
        role = Role("Admin", "admin,read,write", "ADM001")
        user.assign_role(role)
        assert user.role == role
        assert user.username == "john_doe_Admin"

    def test_assign_role_updates_username(self):
        user = User("test_user", "test@example.com", True)
        role = Role("Manager", "read,write", "MGR001")
        user.assign_role(role)
        assert user.username == "test_user_Manager"

    def test_assign_role_replaces_previous(self):
        user = User("john_doe", "john@example.com", True)
        role1 = Role("User", "read", "USR001")
        role2 = Role("Admin", "admin", "ADM001")
        user.assign_role(role1)
        user.assign_role(role2)
        assert user.role == role2
        assert user.username == "john_doe_User_Admin"

    def test_assign_role_invalid_type(self):
        user = User("john_doe", "john@example.com", True)
        with pytest.raises(ValueError, match="Invalid Role object."):
            user.assign_role("not a role")

    def test_assign_role_invalid_type_with_dict(self):
        user = User("john_doe", "john@example.com", True)
        with pytest.raises(ValueError, match="Invalid Role object."):
            user.assign_role({"name": "Admin"})

    def test_assign_role_invalid_type_with_none(self):
        user = User("john_doe", "john@example.com", True)
        with pytest.raises(ValueError, match="Invalid Role object."):
            user.assign_role(None)

    def test_assign_role_without_name_attr(self):
        user = User("john_doe", "john@example.com", True)
        role = Role("Admin", "admin", "ADM001")
        delattr(role, "name")
        user.assign_role(role)
        assert user.role == role
        assert user.username == "john_doe"

    def test_deactivate_regular_user(self):
        user = User("john_doe", "john@example.com", True)
        user.deactivate()
        assert user.active is False

    def test_deactivate_already_inactive(self):
        user = User("john_doe", "john@example.com", False)
        user.deactivate()
        assert user.active is False

    def test_deactivate_admin_user(self):
        user = User("admin_user", "admin@example.com", True)
        role = Role("admin", "admin,read,write", "ADM001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is True

    def test_deactivate_admin_role_uppercase(self):
        user = User("admin_user", "admin@example.com", True)
        role = Role("ADMIN", "admin", "ADM001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is False

    def test_deactivate_admin_role_mixed_case(self):
        user = User("admin_user", "admin@example.com", True)
        role = Role("Admin", "admin", "ADM001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is False

    def test_deactivate_non_admin_role(self):
        user = User("user", "user@example.com", True)
        role = Role("User", "read", "USR001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is False

    def test_deactivate_without_role(self):
        user = User("john_doe", "john@example.com", True)
        user.deactivate()
        assert user.active is False
        assert user.role is None

    def test_deactivate_role_with_admin_in_name(self):
        user = User("user", "user@example.com", True)
        role = Role("administrator", "read,write", "ADM001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is False

    def test_deactivate_preserves_username_and_email(self):
        user = User("john_doe", "john@example.com", True)
        user.deactivate()
        assert user.username == "john_doe"
        assert user.email == "john@example.com"

    def test_assign_role_preserves_email_and_active(self):
        user = User("john_doe", "john@example.com", True)
        role = Role("Manager", "read,write", "MGR001")
        user.assign_role(role)
        assert user.email == "john@example.com"
        assert user.active is True

    def test_multiple_role_assignments(self):
        user = User("user", "user@example.com", True)
        role1 = Role("Role1", "read", "R1")
        role2 = Role("Role2", "write", "R2")
        role3 = Role("Role3", "delete", "R3")
        user.assign_role(role1)
        user.assign_role(role2)
        user.assign_role(role3)
        assert user.username == "user_Role1_Role2_Role3"
        assert user.role == role3

    def test_assign_role_and_deactivate_admin(self):
        user = User("admin", "admin@example.com", True)
        role = Role("admin", "admin", "ADM001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is True
        assert user.username == "admin_admin"

    def test_assign_role_and_deactivate_non_admin(self):
        user = User("user", "user@example.com", True)
        role = Role("user", "read", "USR001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is False
        assert user.username == "user_user"

    def test_deactivate_multiple_times(self):
        user = User("user", "user@example.com", True)
        user.deactivate()
        assert user.active is False
        user.deactivate()
        assert user.active is False

    def test_deactivate_admin_multiple_times(self):
        user = User("admin", "admin@example.com", True)
        role = Role("admin", "admin", "ADM001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is True
        user.deactivate()
        assert user.active is True

    def test_assign_role_empty_name(self):
        user = User("user", "user@example.com", True)
        role = Role("", "read", "R1")
        user.assign_role(role)
        assert user.username == "user_"

    def test_deactivate_role_name_contains_admin(self):
        user = User("user", "user@example.com", True)
        role = Role("superadmin", "all", "SA001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is False

    def test_deactivate_role_name_admin_substring(self):
        user = User("user", "user@example.com", True)
        role = Role("adminuser", "read", "AU001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is False

    def test_deactivate_after_inactive_with_admin_role(self):
        user = User("admin", "admin@example.com", False)
        role = Role("admin", "admin", "ADM001")
        user.assign_role(role)
        user.deactivate()
        assert user.active is True

    def test_assign_role_with_special_characters(self):
        user = User("user", "user@example.com", True)
        role = Role("Admin-Manager", "admin", "AM001")
        user.assign_role(role)
        assert user.username == "user_Admin-Manager"

    def test_username_with_underscores(self):
        user = User("test_user_name", "test@example.com", True)
        role = Role("TestRole", "read", "TR001")
        user.assign_role(role)
        assert user.username == "test_user_name_TestRole"

    def test_deactivate_checks_exact_role_name(self):
        user = User("user", "user@example.com", True)
        role = Role("admin", "read", "R1")
        user.assign_role(role)
        user.deactivate()
        assert user.active is True
