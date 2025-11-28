import pytest
from booking_management.DiscountException import DiscountException


class TestDiscountException:
    def test_raise_exception(self):
        with pytest.raises(DiscountException):
            raise DiscountException("Discount error")

    def test_exception_message(self):
        with pytest.raises(DiscountException, match="Discount error"):
            raise DiscountException("Discount error")

    def test_exception_is_exception(self):
        assert issubclass(DiscountException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(DiscountException):
            raise DiscountException()

    def test_exception_inheritance(self):
        try:
            raise DiscountException("Error")
        except Exception as e:
            assert isinstance(e, DiscountException)
