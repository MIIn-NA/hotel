import pytest
from core.Logger import Logger


class TestLogger:
    def test_init(self):
        logger = Logger("info", "APP", True)
        assert logger.log_level == "info"
        assert logger.prefix == "APP"
        assert logger.enabled is True

    def test_log_enabled(self):
        logger = Logger("info", "APP", True)
        result = logger.log("test message")
        assert result == "[INFO] APP:test message"

    def test_log_disabled(self):
        logger = Logger("info", "APP", False)
        result = logger.log("test message")
        assert result == ""

    def test_log_formatting(self):
        logger = Logger("debug", "SYS", True)
        result = logger.log("testing")
        assert result == "[DEBUG] SYS:testing"

    def test_log_with_colons_in_message(self):
        logger = Logger("error", "DB", True)
        result = logger.log("connection: failed: timeout")
        assert result == "[ERROR] DB:connection:failed:timeout"

    def test_change_level_to_debug(self):
        logger = Logger("info", "APP", True)
        logger.change_level("debug")
        assert logger.log_level == "debug"

    def test_change_level_to_error(self):
        logger = Logger("info", "APP", True)
        logger.change_level("error")
        assert logger.log_level == "error"

    def test_change_level_case_insensitive(self):
        logger = Logger("info", "APP", True)
        logger.change_level("WARNING")
        assert logger.log_level == "warning"

    def test_change_level_invalid(self):
        logger = Logger("info", "APP", True)
        logger.change_level("invalid")
        assert logger.log_level == "info"

    def test_change_level_not_string(self):
        logger = Logger("info", "APP", True)
        with pytest.raises(ValueError, match="Log level must be a string"):
            logger.change_level(123)

    def test_log_level_uppercase_formatting(self):
        logger = Logger("warning", "TEST", True)
        result = logger.log("alert")
        assert "[WARNING]" in result
