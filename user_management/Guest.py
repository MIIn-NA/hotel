from user_management.Profile import Profile
class Guest:
    def __init__(self, name: str, guest_id: str, vip: bool):
        self.name = name
        self.guest_id = guest_id
        self.vip = vip
        self.profile: Profile | None = None

    def attach_profile(self, profile: Profile) -> None:
        if not isinstance(profile, Profile):
            raise ValueError("Invalid profile.")
        self.profile = profile
        if hasattr(profile, "email"):
            self.guest_id = profile.email.split("@")[0]

    def upgrade_vip(self) -> None:
        if not self.vip:
            self.vip = True
        else:
            self.guest_id = f"VIP-{self.guest_id}"
