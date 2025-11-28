import pytest
from hotel_entities.Location import Location


class TestLocation:
    def test_init(self):
        location = Location("New York", "USA", "5th Avenue")
        assert location.city == "New York"
        assert location.country == "USA"
        assert location.street == "5th Avenue"

    def test_init_with_empty_strings(self):
        location = Location("", "", "")
        assert location.city == ""
        assert location.country == ""
        assert location.street == ""

    def test_init_with_special_characters(self):
        location = Location("São Paulo", "Brazil", "Avenida Paulista")
        assert location.city == "São Paulo"
        assert location.country == "Brazil"
        assert location.street == "Avenida Paulista"

    def test_full_address(self):
        location = Location("Paris", "France", "Champs-Élysées")
        assert location.full_address() == "Champs-Élysées, Paris, France"

    def test_full_address_format(self):
        location = Location("London", "UK", "Baker Street")
        result = location.full_address()
        assert result.startswith("Baker Street")
        assert "London" in result
        assert result.endswith("UK")

    def test_full_address_with_empty_strings(self):
        location = Location("", "", "")
        assert location.full_address() == ", , "

    def test_full_address_partial_empty(self):
        location = Location("Tokyo", "", "Shibuya")
        assert location.full_address() == "Shibuya, Tokyo, "

    def test_full_address_special_characters(self):
        location = Location("München", "Germany", "Marienplatz 1")
        result = location.full_address()
        assert "München" in result
        assert "Germany" in result
        assert "Marienplatz 1" in result

    def test_matches_city_exact_match(self):
        location = Location("Berlin", "Germany", "Unter den Linden")
        assert location.matches_city("Berlin") is True

    def test_matches_city_case_insensitive_lowercase(self):
        location = Location("Berlin", "Germany", "Unter den Linden")
        assert location.matches_city("berlin") is True

    def test_matches_city_case_insensitive_uppercase(self):
        location = Location("Berlin", "Germany", "Unter den Linden")
        assert location.matches_city("BERLIN") is True

    def test_matches_city_case_insensitive_mixedcase(self):
        location = Location("Berlin", "Germany", "Unter den Linden")
        assert location.matches_city("BeRlIn") is True

    def test_matches_city_no_match(self):
        location = Location("Berlin", "Germany", "Unter den Linden")
        assert location.matches_city("Paris") is False

    def test_matches_city_partial_match(self):
        location = Location("Berlin", "Germany", "Unter den Linden")
        assert location.matches_city("Berl") is False

    def test_matches_city_empty_string(self):
        location = Location("Berlin", "Germany", "Unter den Linden")
        assert location.matches_city("") is False

    def test_matches_city_with_whitespace(self):
        location = Location("New York", "USA", "Broadway")
        assert location.matches_city("new york") is True

    def test_matches_city_with_whitespace_exact(self):
        location = Location("New York", "USA", "Broadway")
        assert location.matches_city("New York") is True

    def test_matches_city_extra_spaces_no_match(self):
        location = Location("New York", "USA", "Broadway")
        assert location.matches_city("New  York") is False  # Double space

    def test_matches_city_empty_city_empty_name(self):
        location = Location("", "USA", "Broadway")
        assert location.matches_city("") is True

    def test_matches_city_special_characters(self):
        location = Location("São Paulo", "Brazil", "Avenida")
        assert location.matches_city("são paulo") is True

    def test_matches_city_special_characters_exact(self):
        location = Location("São Paulo", "Brazil", "Avenida")
        assert location.matches_city("São Paulo") is True

    def test_full_address_consistency(self):
        location = Location("Rome", "Italy", "Via del Corso")
        addr1 = location.full_address()
        addr2 = location.full_address()
        assert addr1 == addr2

    def test_matches_city_does_not_modify_city(self):
        location = Location("Vienna", "Austria", "Ringstraße")
        original_city = location.city
        location.matches_city("vienna")
        assert location.city == original_city

    def test_full_address_does_not_modify_attributes(self):
        location = Location("Madrid", "Spain", "Gran Vía")
        original_city = location.city
        original_country = location.country
        original_street = location.street
        location.full_address()
        assert location.city == original_city
        assert location.country == original_country
        assert location.street == original_street

    def test_matches_city_with_numbers(self):
        location = Location("District 9", "Country", "Street")
        assert location.matches_city("district 9") is True

    def test_full_address_with_numbers(self):
        location = Location("City1", "Country2", "Street3")
        assert location.full_address() == "Street3, City1, Country2"

    def test_matches_city_unicode(self):
        location = Location("北京", "China", "天安门")
        assert location.matches_city("北京") is True

    def test_full_address_unicode(self):
        location = Location("北京", "中国", "天安门")
        result = location.full_address()
        assert "北京" in result
        assert "中国" in result
        assert "天安门" in result
