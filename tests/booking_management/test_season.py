import pytest
from booking_management.Season import Season


class TestSeason:
    def test_init(self):
        season = Season("Summer", "2024-06-01", "2024-08-31")
        assert season.name == "Summer"
        assert season.start == "2024-06-01"
        assert season.end == "2024-08-31"

    def test_is_active_within_range(self):
        season = Season("Summer", "2024-06-01", "2024-08-31")
        assert season.is_active("2024-07-15") is True

    def test_is_active_before_start(self):
        season = Season("Summer", "2024-06-01", "2024-08-31")
        assert season.is_active("2024-05-31") is False

    def test_is_active_after_end(self):
        season = Season("Summer", "2024-06-01", "2024-08-31")
        assert season.is_active("2024-09-01") is False

    def test_is_active_on_start_date(self):
        season = Season("Summer", "2024-06-01", "2024-08-31")
        assert season.is_active("2024-06-01") is True

    def test_is_active_on_end_date(self):
        season = Season("Summer", "2024-06-01", "2024-08-31")
        assert season.is_active("2024-08-31") is True

    def test_length_equal_dates(self):
        season = Season("Winter", "2024-01-01", "2024-03-31")
        assert season.length() == 10

    def test_length_different_date_lengths(self):
        season = Season("Summer", "2024-6-1", "2024-08-31")
        assert season.length() == 10

    def test_length_returns_max(self):
        season = Season("Fall", "2024-9-01", "2024-11-30")
        result = season.length()
        assert result == max(len("2024-9-01"), len("2024-11-30"))

    def test_is_active_string_comparison(self):
        season = Season("Test", "2024-06-01", "2024-08-31")
        assert season.is_active("2024-10-01") is False
        assert season.is_active("2024-07-01") is True
