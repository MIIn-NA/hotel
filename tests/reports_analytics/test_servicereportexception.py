import pytest
from reports_analytics.ServiceReportException import ServiceReportException


class TestServiceReportException:
    def test_raise_exception(self):
        with pytest.raises(ServiceReportException):
            raise ServiceReportException("Service report error")

    def test_exception_message(self):
        with pytest.raises(ServiceReportException, match="Service report error"):
            raise ServiceReportException("Service report error")

    def test_exception_is_exception(self):
        assert issubclass(ServiceReportException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(ServiceReportException):
            raise ServiceReportException()

    def test_exception_inheritance(self):
        try:
            raise ServiceReportException("Error")
        except Exception as e:
            assert isinstance(e, ServiceReportException)

    def test_exception_with_custom_message(self):
        with pytest.raises(ServiceReportException, match="Custom service error"):
            raise ServiceReportException("Custom service error")

    def test_exception_catch_specific(self):
        try:
            raise ServiceReportException("Specific error")
        except ServiceReportException as e:
            assert str(e) == "Specific error"

    def test_exception_multiple_raises(self):
        for i in range(3):
            with pytest.raises(ServiceReportException):
                raise ServiceReportException(f"Error {i}")
