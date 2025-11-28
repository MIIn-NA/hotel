import pytest
from user_management.Profile import Profile


class TestProfile:
    def test_init(self):
        profile = Profile("john@example.com", "555-1234", "123 Main St")
        assert profile.email == "john@example.com"
        assert profile.phone == "555-1234"
        assert profile.address == "123 Main St"

    def test_init_with_different_values(self):
        profile1 = Profile("alice@test.com", "555-0000", "456 Oak Ave")
        profile2 = Profile("bob@domain.org", "555-9999", "789 Pine Rd")
        assert profile1.email == "alice@test.com"
        assert profile2.phone == "555-9999"

    def test_init_with_empty_strings(self):
        profile = Profile("", "", "")
        assert profile.email == ""
        assert profile.phone == ""
        assert profile.address == ""

    def test_masked_email_basic(self):
        profile = Profile("john@example.com", "555-1234", "123 Main St")
        assert profile.masked_email() == "***n@example.com"

    def test_masked_email_short_name(self):
        profile = Profile("a@example.com", "555-1234", "123 Main St")
        assert profile.masked_email() == "a@example.com"

    def test_masked_email_two_char_name(self):
        profile = Profile("ab@example.com", "555-1234", "123 Main St")
        assert profile.masked_email() == "*b@example.com"

    def test_masked_email_long_name(self):
        profile = Profile("verylongemail@example.com", "555-1234", "123 Main St")
        assert profile.masked_email() == "************l@example.com"

    def test_masked_email_no_at_symbol(self):
        profile = Profile("invalid_email", "555-1234", "123 Main St")
        assert profile.masked_email() == "invalid_email"

    def test_masked_email_empty_string(self):
        profile = Profile("", "555-1234", "123 Main St")
        assert profile.masked_email() == ""

    def test_masked_email_only_at_symbol(self):
        profile = Profile("@", "555-1234", "123 Main St")
        with pytest.raises(IndexError):
            profile.masked_email()

    def test_masked_email_empty_name_part(self):
        profile = Profile("@example.com", "555-1234", "123 Main St")
        with pytest.raises(IndexError):
            profile.masked_email()

    def test_masked_email_multiple_at_symbols(self):
        profile = Profile("test@test@example.com", "555-1234", "123 Main St")
        with pytest.raises(ValueError):
            profile.masked_email()

    def test_masked_email_with_dots(self):
        profile = Profile("first.last@example.com", "555-1234", "123 Main St")
        assert profile.masked_email() == "*********t@example.com"

    def test_masked_email_with_numbers(self):
        profile = Profile("user123@example.com", "555-1234", "123 Main St")
        assert profile.masked_email() == "******3@example.com"

    def test_short_address_basic(self):
        profile = Profile("john@example.com", "555-1234", "123 Main St City State")
        assert profile.short_address() == "123 Main St"

    def test_short_address_exactly_three_words(self):
        profile = Profile("john@example.com", "555-1234", "123 Main St")
        assert profile.short_address() == "123 Main St"

    def test_short_address_less_than_three_words(self):
        profile = Profile("john@example.com", "555-1234", "Main St")
        assert profile.short_address() == "Main St"

    def test_short_address_one_word(self):
        profile = Profile("john@example.com", "555-1234", "Address")
        assert profile.short_address() == "Address"

    def test_short_address_empty_string(self):
        profile = Profile("john@example.com", "555-1234", "")
        assert profile.short_address() == ""

    def test_short_address_many_words(self):
        profile = Profile("john@example.com", "555-1234", "123 Main St City State Zip Country")
        assert profile.short_address() == "123 Main St"

    def test_short_address_with_extra_spaces(self):
        profile = Profile("john@example.com", "555-1234", "123  Main  St  City")
        result = profile.short_address()
        parts = result.split()
        assert len(parts) == 3

    def test_short_address_leading_trailing_spaces(self):
        profile = Profile("john@example.com", "555-1234", "  123 Main St City  ")
        result = profile.short_address()
        assert result.strip() == result

    def test_masked_email_and_short_address(self):
        profile = Profile("john@example.com", "555-1234", "123 Main St City State")
        masked = profile.masked_email()
        short = profile.short_address()
        assert masked == "***n@example.com"
        assert short == "123 Main St"

    def test_multiple_masked_email_calls(self):
        profile = Profile("test@example.com", "555-1234", "Address")
        result1 = profile.masked_email()
        result2 = profile.masked_email()
        assert result1 == result2
        assert result1 == "***t@example.com"

    def test_multiple_short_address_calls(self):
        profile = Profile("test@example.com", "555-1234", "123 Main St City")
        result1 = profile.short_address()
        result2 = profile.short_address()
        assert result1 == result2
        assert result1 == "123 Main St"

    def test_email_modification_affects_masked_email(self):
        profile = Profile("short@example.com", "555-1234", "Address")
        masked1 = profile.masked_email()
        profile.email = "verylongemail@example.com"
        masked2 = profile.masked_email()
        assert masked1 == "****t@example.com"
        assert masked2 == "************l@example.com"

    def test_address_modification_affects_short_address(self):
        profile = Profile("test@example.com", "555-1234", "Short")
        short1 = profile.short_address()
        profile.address = "123 Main St City State"
        short2 = profile.short_address()
        assert short1 == "Short"
        assert short2 == "123 Main St"

    def test_masked_email_with_special_characters(self):
        profile = Profile("user+tag@example.com", "555-1234", "Address")
        assert profile.masked_email() == "*******g@example.com"

    def test_short_address_with_special_characters(self):
        profile = Profile("test@example.com", "555-1234", "123-A Main St. Apt#5")
        assert profile.short_address() == "123-A Main St."

    def test_masked_email_preserves_domain(self):
        profile = Profile("user@subdomain.example.com", "555-1234", "Address")
        masked = profile.masked_email()
        assert masked.endswith("@subdomain.example.com")

    def test_short_address_single_space(self):
        profile = Profile("test@example.com", "555-1234", "A B C D E F")
        assert profile.short_address() == "A B C"
