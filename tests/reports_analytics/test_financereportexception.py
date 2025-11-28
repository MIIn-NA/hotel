import pytest
from reports_analytics.FinanceReportException import FinanceReportException


class TestFinanceReportException:
    def test_raise_exception(self):
        with pytest.raises(FinanceReportException):
            raise FinanceReportException("Finance report error")

    def test_exception_message(self):
        with pytest.raises(FinanceReportException, match="Finance report error"):
            raise FinanceReportException("Finance report error")

    def test_exception_is_exception(self):
        assert issubclass(FinanceReportException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(FinanceReportException):
            raise FinanceReportException()

    def test_exception_inheritance(self):
        try:
            raise FinanceReportException("Error")
        except Exception as e:
            assert isinstance(e, FinanceReportException)

    def test_exception_with_custom_message(self):
        with pytest.raises(FinanceReportException, match="Custom finance error"):
            raise FinanceReportException("Custom finance error")

    def test_exception_catch_specific(self):
        try:
            raise FinanceReportException("Specific error")
        except FinanceReportException as e:
            assert str(e) == "Specific error"

    def test_exception_multiple_raises(self):
        for i in range(3):
            with pytest.raises(FinanceReportException):
                raise FinanceReportException(f"Error {i}")
