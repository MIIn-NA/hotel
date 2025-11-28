import pytest
from booking_management.InvoiceException import InvoiceException


class TestInvoiceException:
    def test_raise_exception(self):
        with pytest.raises(InvoiceException):
            raise InvoiceException("Invoice error")

    def test_exception_message(self):
        with pytest.raises(InvoiceException, match="Invoice error"):
            raise InvoiceException("Invoice error")

    def test_exception_is_exception(self):
        assert issubclass(InvoiceException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(InvoiceException):
            raise InvoiceException()

    def test_exception_inheritance(self):
        try:
            raise InvoiceException("Error")
        except Exception as e:
            assert isinstance(e, InvoiceException)
