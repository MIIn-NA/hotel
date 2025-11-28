import pytest
from core.Notifier import Notifier


class TestNotifier:
    def test_init(self):
        notifier = Notifier("email", "system@hotel.com", True)
        assert notifier.channel == "email"
        assert notifier.sender == "system@hotel.com"
        assert notifier.enabled is True

    def test_send_email_enabled(self):
        notifier = Notifier("email", "system@hotel.com", True)
        result = notifier.send("user@example.com", "Welcome")
        assert result is True

    def test_send_disabled(self):
        notifier = Notifier("email", "system@hotel.com", False)
        result = notifier.send("user@example.com", "Welcome")
        assert result is False

    def test_send_wrong_channel(self):
        notifier = Notifier("sms", "system@hotel.com", True)
        result = notifier.send("user@example.com", "Welcome")
        assert result is False

    def test_send_invalid_email(self):
        notifier = Notifier("email", "system@hotel.com", True)
        result = notifier.send("invalid-email", "Welcome")
        assert result is False

    def test_send_message_length_check(self):
        notifier = Notifier("email", "sys", True)
        result = notifier.send("a@b.c", "hi")
        assert result is True

    def test_prepare_message_basic(self):
        notifier = Notifier("email", "system@hotel.com", True)
        result = notifier.prepare_message("hello world")
        assert result == "Hello world"

    def test_prepare_message_strip_whitespace(self):
        notifier = Notifier("email", "system@hotel.com", True)
        result = notifier.prepare_message("  test  ")
        assert result == "Test"

    def test_prepare_message_capitalize(self):
        notifier = Notifier("email", "system@hotel.com", True)
        result = notifier.prepare_message("lowercase")
        assert result == "Lowercase"

    def test_prepare_message_too_short(self):
        notifier = Notifier("email", "system@hotel.com", True)
        result = notifier.prepare_message("ab")
        assert result == "Ab..."

    def test_prepare_message_empty(self):
        notifier = Notifier("email", "system@hotel.com", True)
        result = notifier.prepare_message("")
        assert result == "..."
