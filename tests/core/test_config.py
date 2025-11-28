import pytest
from core.Config import Config


class TestConfig:
    def test_init(self):
        config = Config("production", False, "1.0.0")
        assert config.environment == "production"
        assert config.debug is False
        assert config.version == "1.0.0"

    def test_is_production_true(self):
        config = Config("production", False, "1.0.0")
        assert config.is_production() is True

    def test_is_production_false_with_debug(self):
        config = Config("production", True, "1.0.0")
        assert config.is_production() is False

    def test_is_production_false_wrong_env(self):
        config = Config("development", False, "1.0.0")
        assert config.is_production() is False

    def test_is_production_case_insensitive(self):
        config = Config("PRODUCTION", False, "1.0.0")
        assert config.is_production() is True

    def test_merge_version_basic(self):
        config = Config("production", False, "1.0.0")
        result = config.merge_version("beta")
        assert result == "1.0.0-beta"
        assert config.version == "1.0.0-beta"

    def test_merge_version_with_whitespace(self):
        config = Config("production", False, "1.0.0")
        result = config.merge_version("  rc1  ")
        assert result == "1.0.0-rc1"

    def test_merge_version_not_string(self):
        config = Config("production", False, "1.0.0")
        with pytest.raises(ValueError, match="Suffix must be a string"):
            config.merge_version(123)

    def test_merge_version_empty_string(self):
        config = Config("production", False, "1.0.0")
        result = config.merge_version("")
        assert result == "1.0.0-"

    def test_merge_version_updates_internal_version(self):
        config = Config("production", False, "1.0.0")
        config.merge_version("alpha")
        assert config.version == "1.0.0-alpha"
