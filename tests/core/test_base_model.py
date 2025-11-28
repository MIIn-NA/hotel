import pytest
from core.BaseModel import BaseModel


class TestBaseModel:
    def test_init(self):
        model = BaseModel("test123", "2024-01-01", "2024-01-02")
        assert model.identifier == "test123"
        assert model.created_at == "2024-01-01"
        assert model.updated_at == "2024-01-02"

    def test_validate_identifier_valid(self):
        model = BaseModel("test123", "2024-01-01", "2024-01-02")
        assert model.validate_identifier() is True

    def test_validate_identifier_with_special_chars(self):
        model = BaseModel("test@123", "2024-01-01", "2024-01-02")
        assert model.validate_identifier() is False

    def test_validate_identifier_too_short(self):
        model = BaseModel("ab", "2024-01-01", "2024-01-02")
        assert model.validate_identifier() is False

    def test_validate_identifier_not_string(self):
        model = BaseModel(123, "2024-01-01", "2024-01-02")
        with pytest.raises(ValueError, match="Identifier must be a string"):
            model.validate_identifier()

    def test_validate_identifier_whitespace(self):
        model = BaseModel("  abc  ", "2024-01-01", "2024-01-02")
        assert model.validate_identifier() is False

    def test_refresh_updated_at_valid(self):
        model = BaseModel("test123", "2024-01-01", "2024-01-02")
        model.refresh_updated_at("2024-01-03")
        assert model.updated_at == "2024-01-03"

    def test_refresh_updated_at_with_whitespace(self):
        model = BaseModel("test123", "2024-01-01", "2024-01-02")
        model.refresh_updated_at("  2024-01-03  ")
        assert model.updated_at == "2024-01-03"

    def test_refresh_updated_at_not_string(self):
        model = BaseModel("test123", "2024-01-01", "2024-01-02")
        with pytest.raises(ValueError, match="updated_at must be a string timestamp"):
            model.refresh_updated_at(12345)

    def test_refresh_updated_at_too_short(self):
        model = BaseModel("test123", "2024-01-01", "2024-01-02")
        with pytest.raises(ValueError, match="Timestamp format is incorrect"):
            model.refresh_updated_at("123")
