import pytest
from booking_management.Cancellation import Cancellation
from booking_management.Booking import Booking


class TestCancellation:
    def test_init(self):
        cancel = Cancellation("Guest requested", "2024-01-15", 50.0)
        assert cancel.reason == "Guest requested"
        assert cancel.date == "2024-01-15"
        assert cancel.penalty == 50.0
        assert cancel.booking is None

    def test_attach_booking_valid(self):
        cancel = Cancellation("Emergency", "2024-01-15", 30.0)
        booking = Booking("BK001", 3, "confirmed")
        cancel.attach_booking(booking)
        assert cancel.booking == booking

    def test_attach_booking_invalid_type(self):
        cancel = Cancellation("Emergency", "2024-01-15", 30.0)
        with pytest.raises(ValueError, match="Invalid Booking object"):
            cancel.attach_booking("not a booking")

    def test_calculate_penalty_without_booking(self):
        cancel = Cancellation("Late cancel", "2024-01-15", 50.0)
        result = cancel.calculate_penalty()
        assert result == 50.0

    def test_calculate_penalty_with_booking(self):
        cancel = Cancellation("Changed plans", "2024-01-15", 50.0)
        booking = Booking("BK001", 3, "confirmed")
        cancel.attach_booking(booking)
        result = cancel.calculate_penalty()
        expected = len("Changed plans") * 0.5 + 50.0
        assert result == round(expected, 2)

    def test_calculate_penalty_short_reason(self):
        cancel = Cancellation("No", "2024-01-15", 10.0)
        booking = Booking("BK001", 2, "confirmed")
        cancel.attach_booking(booking)
        result = cancel.calculate_penalty()
        expected = len("No") * 0.5 + 10.0
        assert result == 11.0

    def test_calculate_penalty_long_reason(self):
        reason = "Due to unforeseen circumstances and scheduling conflicts"
        cancel = Cancellation(reason, "2024-01-15", 25.0)
        booking = Booking("BK001", 5, "confirmed")
        cancel.attach_booking(booking)
        result = cancel.calculate_penalty()
        expected = len(reason) * 0.5 + 25.0
        assert result == round(expected, 2)

    def test_calculate_penalty_zero_base(self):
        cancel = Cancellation("Cancel", "2024-01-15", 0.0)
        booking = Booking("BK001", 1, "confirmed")
        cancel.attach_booking(booking)
        result = cancel.calculate_penalty()
        assert result == 3.0

    def test_calculate_penalty_empty_reason(self):
        cancel = Cancellation("", "2024-01-15", 20.0)
        booking = Booking("BK001", 2, "confirmed")
        cancel.attach_booking(booking)
        result = cancel.calculate_penalty()
        assert result == 20.0
