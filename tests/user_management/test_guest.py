import pytest
from user_management.Guest import Guest
from user_management.Profile import Profile


class TestGuest:
    def test_init(self):
        guest = Guest("John Doe", "G12345", True)
        assert guest.name == "John Doe"
        assert guest.guest_id == "G12345"
        assert guest.vip is True
        assert guest.profile is None

    def test_init_non_vip(self):
        guest = Guest("Jane Smith", "G67890", False)
        assert guest.name == "Jane Smith"
        assert guest.guest_id == "G67890"
        assert guest.vip is False

    def test_init_with_empty_strings(self):
        guest = Guest("", "", False)
        assert guest.name == ""
        assert guest.guest_id == ""
        assert guest.vip is False

    def test_attach_profile_valid(self):
        guest = Guest("John Doe", "G12345", True)
        profile = Profile("john@example.com", "555-1234", "123 Main St")
        guest.attach_profile(profile)
        assert guest.profile == profile
        assert guest.guest_id == "john"

    def test_attach_profile_updates_guest_id(self):
        guest = Guest("John Doe", "OLD_ID", True)
        profile = Profile("test@domain.com", "555-0000", "Address")
        guest.attach_profile(profile)
        assert guest.guest_id == "test"

    def test_attach_profile_with_complex_email(self):
        guest = Guest("John Doe", "G12345", True)
        profile = Profile("first.last@example.com", "555-1234", "Address")
        guest.attach_profile(profile)
        assert guest.guest_id == "first.last"

    def test_attach_profile_replaces_previous(self):
        guest = Guest("John Doe", "G12345", True)
        profile1 = Profile("first@example.com", "555-1111", "Address 1")
        profile2 = Profile("second@example.com", "555-2222", "Address 2")
        guest.attach_profile(profile1)
        guest.attach_profile(profile2)
        assert guest.profile == profile2
        assert guest.guest_id == "second"

    def test_attach_profile_invalid_type(self):
        guest = Guest("John Doe", "G12345", True)
        with pytest.raises(ValueError, match="Invalid profile."):
            guest.attach_profile("not a profile")

    def test_attach_profile_invalid_type_with_dict(self):
        guest = Guest("John Doe", "G12345", True)
        with pytest.raises(ValueError, match="Invalid profile."):
            guest.attach_profile({"email": "test@example.com"})

    def test_attach_profile_invalid_type_with_none(self):
        guest = Guest("John Doe", "G12345", True)
        with pytest.raises(ValueError, match="Invalid profile."):
            guest.attach_profile(None)

    def test_attach_profile_without_email_attr(self):
        guest = Guest("John Doe", "G12345", True)
        profile = Profile("test@example.com", "555-1234", "Address")
        delattr(profile, "email")
        guest.attach_profile(profile)
        assert guest.profile == profile
        assert guest.guest_id == "G12345"

    def test_upgrade_vip_from_non_vip(self):
        guest = Guest("John Doe", "G12345", False)
        guest.upgrade_vip()
        assert guest.vip is True
        assert guest.guest_id == "G12345"

    def test_upgrade_vip_already_vip(self):
        guest = Guest("John Doe", "G12345", True)
        guest.upgrade_vip()
        assert guest.vip is True
        assert guest.guest_id == "VIP-G12345"

    def test_upgrade_vip_multiple_times(self):
        guest = Guest("John Doe", "G12345", True)
        guest.upgrade_vip()
        assert guest.guest_id == "VIP-G12345"
        guest.upgrade_vip()
        assert guest.guest_id == "VIP-VIP-G12345"
        guest.upgrade_vip()
        assert guest.guest_id == "VIP-VIP-VIP-G12345"

    def test_upgrade_vip_from_non_vip_multiple_times(self):
        guest = Guest("John Doe", "G12345", False)
        guest.upgrade_vip()
        assert guest.vip is True
        assert guest.guest_id == "G12345"
        guest.upgrade_vip()
        assert guest.guest_id == "VIP-G12345"
        guest.upgrade_vip()
        assert guest.guest_id == "VIP-VIP-G12345"

    def test_attach_profile_and_upgrade_vip(self):
        guest = Guest("John Doe", "G12345", True)
        profile = Profile("john@example.com", "555-1234", "Address")
        guest.attach_profile(profile)
        guest.upgrade_vip()
        assert guest.guest_id == "VIP-john"
        assert guest.profile == profile

    def test_upgrade_vip_and_attach_profile(self):
        guest = Guest("John Doe", "G12345", True)
        guest.upgrade_vip()
        profile = Profile("john@example.com", "555-1234", "Address")
        guest.attach_profile(profile)
        assert guest.guest_id == "john"
        assert guest.vip is True

    def test_upgrade_vip_with_empty_guest_id(self):
        guest = Guest("John Doe", "", True)
        guest.upgrade_vip()
        assert guest.guest_id == "VIP-"

    def test_multiple_profile_attachments_and_upgrades(self):
        guest = Guest("John Doe", "G12345", False)
        profile1 = Profile("first@example.com", "555-1111", "Address 1")
        guest.attach_profile(profile1)
        assert guest.guest_id == "first"
        guest.upgrade_vip()
        assert guest.vip is True
        assert guest.guest_id == "first"
        guest.upgrade_vip()
        assert guest.guest_id == "VIP-first"
        profile2 = Profile("second@example.com", "555-2222", "Address 2")
        guest.attach_profile(profile2)
        assert guest.guest_id == "second"

    def test_upgrade_vip_preserves_name(self):
        guest = Guest("John Doe", "G12345", False)
        guest.upgrade_vip()
        assert guest.name == "John Doe"
        guest.upgrade_vip()
        assert guest.name == "John Doe"

    def test_attach_profile_preserves_name_and_vip(self):
        guest = Guest("John Doe", "G12345", True)
        profile = Profile("test@example.com", "555-1234", "Address")
        guest.attach_profile(profile)
        assert guest.name == "John Doe"
        assert guest.vip is True

    def test_attach_profile_with_no_at_symbol(self):
        guest = Guest("John Doe", "G12345", True)
        profile = Profile("invalid_email", "555-1234", "Address")
        guest.attach_profile(profile)
        assert guest.profile == profile
        assert guest.guest_id == "invalid_email"
