import pytest
from reports_analytics.OccupancyReportException import OccupancyReportException


class TestOccupancyReportException:
    def test_raise_exception(self):
        with pytest.raises(OccupancyReportException):
            raise OccupancyReportException("Occupancy report error")

    def test_exception_message(self):
        with pytest.raises(OccupancyReportException, match="Occupancy report error"):
            raise OccupancyReportException("Occupancy report error")

    def test_exception_is_exception(self):
        assert issubclass(OccupancyReportException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(OccupancyReportException):
            raise OccupancyReportException()

    def test_exception_inheritance(self):
        try:
            raise OccupancyReportException("Error")
        except Exception as e:
            assert isinstance(e, OccupancyReportException)

    def test_exception_with_custom_message(self):
        with pytest.raises(OccupancyReportException, match="Custom occupancy error"):
            raise OccupancyReportException("Custom occupancy error")

    def test_exception_catch_specific(self):
        try:
            raise OccupancyReportException("Specific error")
        except OccupancyReportException as e:
            assert str(e) == "Specific error"

    def test_exception_multiple_raises(self):
        for i in range(3):
            with pytest.raises(OccupancyReportException):
                raise OccupancyReportException(f"Error {i}")
