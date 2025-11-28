import pytest
from core.HotelException import HotelException


class TestHotelException:
    def test_raise_exception(self):
        with pytest.raises(HotelException):
            raise HotelException("Test error")

    def test_exception_message(self):
        with pytest.raises(HotelException, match="Test error"):
            raise HotelException("Test error")

    def test_exception_is_exception(self):
        assert issubclass(HotelException, Exception)

    def test_exception_with_empty_message(self):
        with pytest.raises(HotelException):
            raise HotelException()

    def test_exception_inheritance(self):
        try:
            raise HotelException("Error")
        except Exception as e:
            assert isinstance(e, HotelException)
