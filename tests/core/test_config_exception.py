import pytest
from core.ConfigException import ConfigException


class TestConfigException:
    def test_raise_exception(self):
        with pytest.raises(ConfigException):
            raise ConfigException("Config error")

    def test_exception_message(self):
        with pytest.raises(ConfigException, match="Config error"):
            raise ConfigException("Config error")

    def test_exception_is_exception(self):
        assert issubclass(ConfigException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(ConfigException):
            raise ConfigException()

    def test_exception_inheritance(self):
        try:
            raise ConfigException("Error")
        except Exception as e:
            assert isinstance(e, ConfigException)
