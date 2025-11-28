from user_management.Guest import Guest
class Transportation:
    def __init__(self, vehicle: str, driver: str, cost: float):
        self.vehicle = vehicle
        self.driver = driver
        self.cost = cost
        self.passengers: list[Guest] = []

    def add_passenger(self, guest: Guest) -> None:
        if not isinstance(guest, Guest):
            raise ValueError("Invalid Guest.")
        self.passengers.append(guest)
        if guest.vip:
            self.cost += 5

    def passenger_count(self) -> int:
        return len(self.passengers)
