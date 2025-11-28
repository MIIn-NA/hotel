import pytest
from user_management.Permission import Permission


class TestPermission:
    def test_init(self):
        perm = Permission("read", 3, "file")
        assert perm.name == "read"
        assert perm.level == 3
        assert perm.category == "file"

    def test_init_with_different_values(self):
        perm1 = Permission("write", 7, "database")
        perm2 = Permission("delete", 10, "admin")
        assert perm1.name == "write"
        assert perm1.level == 7
        assert perm2.category == "admin"

    def test_init_with_zero_level(self):
        perm = Permission("view", 0, "public")
        assert perm.level == 0

    def test_init_with_negative_level(self):
        perm = Permission("restricted", -5, "special")
        assert perm.level == -5

    def test_init_with_empty_strings(self):
        perm = Permission("", 1, "")
        assert perm.name == ""
        assert perm.category == ""

    def test_is_high_level_5(self):
        perm = Permission("admin", 5, "system")
        assert perm.is_high() is True

    def test_is_high_level_above_5(self):
        perm = Permission("superadmin", 10, "system")
        assert perm.is_high() is True

    def test_is_high_level_6(self):
        perm = Permission("manager", 6, "department")
        assert perm.is_high() is True

    def test_is_high_level_4(self):
        perm = Permission("user", 4, "basic")
        assert perm.is_high() is False

    def test_is_high_level_below_5(self):
        perm = Permission("guest", 1, "public")
        assert perm.is_high() is False

    def test_is_high_level_0(self):
        perm = Permission("none", 0, "public")
        assert perm.is_high() is False

    def test_is_high_negative_level(self):
        perm = Permission("revoked", -3, "special")
        assert perm.is_high() is False

    def test_summary_basic(self):
        perm = Permission("read", 3, "file")
        assert perm.summary() == "read: file (lvl 3)"

    def test_summary_high_level(self):
        perm = Permission("admin", 10, "system")
        assert perm.summary() == "admin: system (lvl 10)"

    def test_summary_zero_level(self):
        perm = Permission("public", 0, "general")
        assert perm.summary() == "public: general (lvl 0)"

    def test_summary_negative_level(self):
        perm = Permission("restricted", -5, "special")
        assert perm.summary() == "restricted: special (lvl -5)"

    def test_summary_with_empty_strings(self):
        perm = Permission("", 1, "")
        assert perm.summary() == ":  (lvl 1)"

    def test_summary_format_consistency(self):
        perm = Permission("write", 5, "database")
        summary = perm.summary()
        assert "write" in summary
        assert "database" in summary
        assert "5" in summary
        assert summary.count("(") == 1
        assert summary.count(")") == 1

    def test_is_high_boundary_exactly_5(self):
        perm = Permission("boundary", 5, "test")
        assert perm.is_high() is True

    def test_is_high_boundary_just_below_5(self):
        perm = Permission("boundary", 4, "test")
        assert perm.is_high() is False

    def test_multiple_permissions_different_levels(self):
        perm1 = Permission("low", 1, "cat1")
        perm2 = Permission("medium", 4, "cat2")
        perm3 = Permission("high", 5, "cat3")
        perm4 = Permission("very_high", 10, "cat4")
        assert perm1.is_high() is False
        assert perm2.is_high() is False
        assert perm3.is_high() is True
        assert perm4.is_high() is True

    def test_summary_with_special_characters(self):
        perm = Permission("read/write", 5, "file-system")
        assert perm.summary() == "read/write: file-system (lvl 5)"

    def test_summary_with_spaces(self):
        perm = Permission("full access", 8, "admin panel")
        assert perm.summary() == "full access: admin panel (lvl 8)"

    def test_is_high_with_large_level(self):
        perm = Permission("ultimate", 1000, "supreme")
        assert perm.is_high() is True

    def test_level_changes(self):
        perm = Permission("dynamic", 3, "test")
        assert perm.is_high() is False
        perm.level = 5
        assert perm.is_high() is True
        perm.level = 10
        assert perm.is_high() is True
        perm.level = 0
        assert perm.is_high() is False

    def test_summary_after_modifications(self):
        perm = Permission("test", 1, "category")
        summary1 = perm.summary()
        perm.level = 10
        summary2 = perm.summary()
        perm.name = "modified"
        summary3 = perm.summary()
        assert summary1 == "test: category (lvl 1)"
        assert summary2 == "test: category (lvl 10)"
        assert summary3 == "modified: category (lvl 10)"
