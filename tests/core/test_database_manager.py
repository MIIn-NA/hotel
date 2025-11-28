import pytest
from core.DatabaseManager import DatabaseManager


class TestDatabaseManager:
    def test_init(self):
        db = DatabaseManager("mysql://localhost:3306/db", 30, 3)
        assert db.connection_string == "mysql://localhost:3306/db"
        assert db.timeout == 30
        assert db.retries == 3

    def test_connect_valid_connection_string(self):
        db = DatabaseManager("mysql://localhost:3306/db", 30, 3)
        result = db.connect()
        assert result is True

    def test_connect_invalid_connection_string(self):
        db = DatabaseManager("invalid_string", 30, 3)
        result = db.connect()
        assert result is False

    def test_connect_retries(self):
        db = DatabaseManager("no_protocol", 30, 5)
        result = db.connect()
        assert result is False

    def test_connect_with_different_protocols(self):
        db = DatabaseManager("postgresql://localhost/mydb", 30, 3)
        result = db.connect()
        assert result is True

    def test_execute_query_basic(self):
        db = DatabaseManager("mysql://localhost/db", 30, 3)
        result = db.execute_query("SELECT name FROM users WHERE active")
        assert "NAME" in result
        assert "FROM" in result
        assert "USERS" in result
        assert "WHERE" in result
        assert "ACTIVE" in result

    def test_execute_query_filters_short_words(self):
        db = DatabaseManager("mysql://localhost/db", 30, 3)
        result = db.execute_query("SELECT id FROM users")
        assert "FROM" in result
        assert "USERS" in result
        assert "id" not in result

    def test_execute_query_not_string(self):
        db = DatabaseManager("mysql://localhost/db", 30, 3)
        with pytest.raises(ValueError, match="Query must be a string"):
            db.execute_query(123)

    def test_execute_query_empty(self):
        db = DatabaseManager("mysql://localhost/db", 30, 3)
        result = db.execute_query("")
        assert result == []

    def test_execute_query_uppercase_conversion(self):
        db = DatabaseManager("mysql://localhost/db", 30, 3)
        result = db.execute_query("select username from accounts")
        assert all(word.isupper() for word in result)
