class Location:
    def __init__(self, city: str, country: str, street: str):
        self.city = city
        self.country = country
        self.street = street

    def full_address(self) -> str:
        return f"{self.street}, {self.city}, {self.country}"

    def matches_city(self, name: str) -> bool:
        return self.city.lower() == name.lower()
