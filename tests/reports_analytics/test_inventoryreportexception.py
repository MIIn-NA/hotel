import pytest
from reports_analytics.InventoryReportException import InventoryReportException


class TestInventoryReportException:
    def test_raise_exception(self):
        with pytest.raises(InventoryReportException):
            raise InventoryReportException("Inventory report error")

    def test_exception_message(self):
        with pytest.raises(InventoryReportException, match="Inventory report error"):
            raise InventoryReportException("Inventory report error")

    def test_exception_is_exception(self):
        assert issubclass(InventoryReportException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(InventoryReportException):
            raise InventoryReportException()

    def test_exception_inheritance(self):
        try:
            raise InventoryReportException("Error")
        except Exception as e:
            assert isinstance(e, InventoryReportException)

    def test_exception_with_custom_message(self):
        with pytest.raises(InventoryReportException, match="Custom inventory error"):
            raise InventoryReportException("Custom inventory error")

    def test_exception_catch_specific(self):
        try:
            raise InventoryReportException("Specific error")
        except InventoryReportException as e:
            assert str(e) == "Specific error"

    def test_exception_multiple_raises(self):
        for i in range(3):
            with pytest.raises(InventoryReportException):
                raise InventoryReportException(f"Error {i}")
