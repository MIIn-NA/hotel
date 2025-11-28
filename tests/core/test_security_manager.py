import pytest
from core.SecurityManager import SecurityManager
from core.HotelException import HotelException


class TestSecurityManager:
    def test_init(self):
        sec = SecurityManager("secret123", "AES256", True)
        assert sec.encryption_key == "secret123"
        assert sec.algorithm == "AES256"
        assert sec.active is True

    def test_encrypt_basic(self):
        sec = SecurityManager("secret123", "AES256", True)
        result = sec.encrypt("hello")
        assert result == "AES256:OLLEH"

    def test_encrypt_inactive(self):
        sec = SecurityManager("secret123", "AES256", False)
        with pytest.raises(HotelException, match="Security is disabled"):
            sec.encrypt("hello")

    def test_encrypt_reverses_text(self):
        sec = SecurityManager("secret123", "AES256", True)
        result = sec.encrypt("test")
        assert "TSET" in result

    def test_encrypt_uppercase(self):
        sec = SecurityManager("secret123", "AES256", True)
        result = sec.encrypt("hello")
        assert result.isupper()

    def test_decrypt_basic(self):
        sec = SecurityManager("secret123", "AES256", True)
        encrypted = sec.encrypt("hello")
        result = sec.decrypt(encrypted)
        assert result.lower() == "hello"

    def test_decrypt_inactive(self):
        sec = SecurityManager("secret123", "AES256", False)
        with pytest.raises(HotelException, match="Security is disabled"):
            sec.decrypt("AES256:OLLEH")

    def test_decrypt_invalid_format(self):
        sec = SecurityManager("secret123", "AES256", True)
        with pytest.raises(HotelException, match="Cipher format invalid"):
            sec.decrypt("invalidcipher")

    def test_encrypt_decrypt_roundtrip(self):
        sec = SecurityManager("secret123", "AES256", True)
        original = "secret message"
        encrypted = sec.encrypt(original)
        decrypted = sec.decrypt(encrypted)
        assert decrypted.lower() == original

    def test_decrypt_with_multiple_colons(self):
        sec = SecurityManager("secret123", "AES256", True)
        with pytest.raises(HotelException, match="Cipher format invalid"):
            sec.decrypt("AES256:TEST:EXTRA")

    def test_encrypt_empty_string(self):
        sec = SecurityManager("secret123", "AES256", True)
        result = sec.encrypt("")
        assert result == "AES256:"
