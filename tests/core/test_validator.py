import pytest
from core.Validator import Validator


class TestValidator:
    def test_init(self):
        validator = Validator(3, 10, False)
        assert validator.min_length == 3
        assert validator.max_length == 10
        assert validator.allow_empty is False

    def test_validate_text_valid(self):
        validator = Validator(3, 10, False)
        assert validator.validate_text("hello") is True

    def test_validate_text_too_short(self):
        validator = Validator(3, 10, False)
        assert validator.validate_text("ab") is False

    def test_validate_text_too_long(self):
        validator = Validator(3, 10, False)
        assert validator.validate_text("this is too long") is False

    def test_validate_text_exact_min_length(self):
        validator = Validator(3, 10, False)
        assert validator.validate_text("abc") is True

    def test_validate_text_exact_max_length(self):
        validator = Validator(3, 10, False)
        assert validator.validate_text("0123456789") is True

    def test_validate_text_empty_allowed(self):
        validator = Validator(3, 10, True)
        assert validator.validate_text("") is True

    def test_validate_text_empty_not_allowed(self):
        validator = Validator(3, 10, False)
        assert validator.validate_text("") is False

    def test_validate_text_not_string(self):
        validator = Validator(3, 10, False)
        with pytest.raises(ValueError, match="Text must be a string"):
            validator.validate_text(123)

    def test_normalize_text_basic(self):
        validator = Validator(3, 10, False)
        result = validator.normalize_text("  hello  world  ")
        assert result == "hello world"

    def test_normalize_text_multiple_spaces(self):
        validator = Validator(3, 10, False)
        result = validator.normalize_text("hello    world")
        assert result == "hello world"

    def test_normalize_text_empty_not_allowed(self):
        validator = Validator(3, 10, False)
        with pytest.raises(ValueError, match="Text cannot be empty"):
            validator.normalize_text("   ")

    def test_normalize_text_empty_allowed(self):
        validator = Validator(3, 10, True)
        result = validator.normalize_text("   ")
        assert result == ""

    def test_normalize_text_not_string(self):
        validator = Validator(3, 10, False)
        with pytest.raises(ValueError, match="Text must be a string"):
            validator.normalize_text(123)
