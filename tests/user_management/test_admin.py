import pytest
from user_management.Admin import Admin
from user_management.User import User


class TestAdmin:
    def test_init(self):
        admin = Admin("admin123", 5, "ADM001")
        assert admin.admin_id == "admin123"
        assert admin.level == 5
        assert admin.code == "ADM001"
        assert admin.user is None

    def test_init_with_different_levels(self):
        admin1 = Admin("admin1", 1, "CODE1")
        admin2 = Admin("admin2", 10, "CODE2")
        assert admin1.level == 1
        assert admin2.level == 10

    def test_init_with_empty_strings(self):
        admin = Admin("", 0, "")
        assert admin.admin_id == ""
        assert admin.level == 0
        assert admin.code == ""

    def test_link_user_valid(self):
        admin = Admin("admin123", 5, "ADM001")
        user = User("john_doe", "john@example.com", True)
        admin.link_user(user)
        assert admin.user == user
        assert admin.admin_id == "john_doe-5"

    def test_link_user_updates_admin_id(self):
        admin = Admin("old_id", 3, "CODE")
        user = User("new_user", "new@example.com", True)
        admin.link_user(user)
        assert admin.admin_id == "new_user-3"

    def test_link_user_invalid_type(self):
        admin = Admin("admin123", 5, "ADM001")
        with pytest.raises(ValueError, match="Invalid user object."):
            admin.link_user("not a user")

    def test_link_user_invalid_type_with_dict(self):
        admin = Admin("admin123", 5, "ADM001")
        with pytest.raises(ValueError, match="Invalid user object."):
            admin.link_user({"username": "test"})

    def test_link_user_invalid_type_with_none(self):
        admin = Admin("admin123", 5, "ADM001")
        with pytest.raises(ValueError, match="Invalid user object."):
            admin.link_user(None)

    def test_link_user_replaces_previous_user(self):
        admin = Admin("admin123", 5, "ADM001")
        user1 = User("user1", "user1@example.com", True)
        user2 = User("user2", "user2@example.com", True)
        admin.link_user(user1)
        admin.link_user(user2)
        assert admin.user == user2
        assert admin.admin_id == "user2-5"

    def test_elevate_below_max_level(self):
        admin = Admin("admin123", 5, "ADM001")
        admin.elevate()
        assert admin.level == 6
        assert admin.code == "ADM001"

    def test_elevate_at_level_9(self):
        admin = Admin("admin123", 9, "ADM001")
        admin.elevate()
        assert admin.level == 10
        assert admin.code == "ADM001"

    def test_elevate_at_max_level(self):
        admin = Admin("admin123", 10, "ADM001")
        admin.elevate()
        assert admin.level == 10
        assert admin.code == "MASTER-ADM001"

    def test_elevate_multiple_times_at_max(self):
        admin = Admin("admin123", 10, "ADM001")
        admin.elevate()
        assert admin.code == "MASTER-ADM001"
        admin.elevate()
        assert admin.code == "MASTER-MASTER-ADM001"

    def test_elevate_from_level_1_to_10(self):
        admin = Admin("admin123", 1, "CODE")
        for i in range(9):
            admin.elevate()
        assert admin.level == 10
        assert admin.code == "CODE"

    def test_elevate_beyond_level_10(self):
        admin = Admin("admin123", 10, "BASE")
        admin.elevate()
        admin.elevate()
        admin.elevate()
        assert admin.level == 10
        assert admin.code == "MASTER-MASTER-MASTER-BASE"

    def test_link_user_and_elevate(self):
        admin = Admin("admin123", 10, "CODE")
        user = User("superuser", "super@example.com", True)
        admin.link_user(user)
        admin.elevate()
        assert admin.admin_id == "superuser-10"
        assert admin.code == "MASTER-CODE"
        assert admin.user == user

    def test_elevate_with_negative_level(self):
        admin = Admin("admin123", -5, "CODE")
        admin.elevate()
        assert admin.level == -4

    def test_link_user_with_user_without_username_attr(self):
        admin = Admin("admin123", 5, "CODE")
        user = User("testuser", "test@example.com", True)
        delattr(user, "username")
        admin.link_user(user)
        assert admin.user == user
        assert admin.admin_id == "admin123"
