import pytest
from reports_analytics.GuestReportException import GuestReportException


class TestGuestReportException:
    def test_raise_exception(self):
        with pytest.raises(GuestReportException):
            raise GuestReportException("Guest report error")

    def test_exception_message(self):
        with pytest.raises(GuestReportException, match="Guest report error"):
            raise GuestReportException("Guest report error")

    def test_exception_is_exception(self):
        assert issubclass(GuestReportException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(GuestReportException):
            raise GuestReportException()

    def test_exception_inheritance(self):
        try:
            raise GuestReportException("Error")
        except Exception as e:
            assert isinstance(e, GuestReportException)

    def test_exception_with_custom_message(self):
        with pytest.raises(GuestReportException, match="Custom guest error"):
            raise GuestReportException("Custom guest error")

    def test_exception_catch_specific(self):
        try:
            raise GuestReportException("Specific error")
        except GuestReportException as e:
            assert str(e) == "Specific error"

    def test_exception_multiple_raises(self):
        for i in range(3):
            with pytest.raises(GuestReportException):
                raise GuestReportException(f"Error {i}")
