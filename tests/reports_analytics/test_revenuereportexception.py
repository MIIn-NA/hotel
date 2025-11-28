import pytest
from reports_analytics.RevenueReportException import RevenueReportException


class TestRevenueReportException:
    def test_raise_exception(self):
        with pytest.raises(RevenueReportException):
            raise RevenueReportException("Revenue report error")

    def test_exception_message(self):
        with pytest.raises(RevenueReportException, match="Revenue report error"):
            raise RevenueReportException("Revenue report error")

    def test_exception_is_exception(self):
        assert issubclass(RevenueReportException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(RevenueReportException):
            raise RevenueReportException()

    def test_exception_inheritance(self):
        try:
            raise RevenueReportException("Error")
        except Exception as e:
            assert isinstance(e, RevenueReportException)

    def test_exception_with_custom_message(self):
        with pytest.raises(RevenueReportException, match="Custom revenue error"):
            raise RevenueReportException("Custom revenue error")

    def test_exception_catch_specific(self):
        try:
            raise RevenueReportException("Specific error")
        except RevenueReportException as e:
            assert str(e) == "Specific error"

    def test_exception_multiple_raises(self):
        for i in range(3):
            with pytest.raises(RevenueReportException):
                raise RevenueReportException(f"Error {i}")
