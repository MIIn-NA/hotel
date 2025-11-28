import pytest
from reports_analytics.AnalyticsException import AnalyticException


class TestAnalyticException:
    def test_raise_exception(self):
        with pytest.raises(AnalyticException):
            raise AnalyticException("Analytics error")

    def test_exception_message(self):
        with pytest.raises(AnalyticException, match="Analytics error"):
            raise AnalyticException("Analytics error")

    def test_exception_is_exception(self):
        assert issubclass(AnalyticException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(AnalyticException):
            raise AnalyticException()

    def test_exception_inheritance(self):
        try:
            raise AnalyticException("Error")
        except Exception as e:
            assert isinstance(e, AnalyticException)

    def test_exception_with_custom_message(self):
        with pytest.raises(AnalyticException, match="Custom analytics error message"):
            raise AnalyticException("Custom analytics error message")

    def test_exception_catch_specific(self):
        try:
            raise AnalyticException("Specific error")
        except AnalyticException as e:
            assert str(e) == "Specific error"

    def test_exception_multiple_raises(self):
        for i in range(3):
            with pytest.raises(AnalyticException):
                raise AnalyticException(f"Error {i}")
