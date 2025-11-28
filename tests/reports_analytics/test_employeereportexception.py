import pytest
from reports_analytics.EmployeeReportException import EmployeeReportException


class TestEmployeeReportException:
    def test_raise_exception(self):
        with pytest.raises(EmployeeReportException):
            raise EmployeeReportException("Employee report error")

    def test_exception_message(self):
        with pytest.raises(EmployeeReportException, match="Employee report error"):
            raise EmployeeReportException("Employee report error")

    def test_exception_is_exception(self):
        assert issubclass(EmployeeReportException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(EmployeeReportException):
            raise EmployeeReportException()

    def test_exception_inheritance(self):
        try:
            raise EmployeeReportException("Error")
        except Exception as e:
            assert isinstance(e, EmployeeReportException)

    def test_exception_with_custom_message(self):
        with pytest.raises(EmployeeReportException, match="Custom employee error"):
            raise EmployeeReportException("Custom employee error")

    def test_exception_catch_specific(self):
        try:
            raise EmployeeReportException("Specific error")
        except EmployeeReportException as e:
            assert str(e) == "Specific error"

    def test_exception_multiple_raises(self):
        for i in range(3):
            with pytest.raises(EmployeeReportException):
                raise EmployeeReportException(f"Error {i}")
