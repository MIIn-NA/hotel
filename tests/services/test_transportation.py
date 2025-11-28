import pytest
from services.Transportation import Transportation
from user_management.Guest import Guest


class TestTransportation:
    def test_init(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        assert transport.vehicle == "Sedan"
        assert transport.driver == "John Driver"
        assert transport.cost == 50.0
        assert transport.passengers == []

    def test_init_with_different_values(self):
        transport = Transportation("SUV", "Jane Driver", 75.0)
        assert transport.vehicle == "SUV"
        assert transport.driver == "Jane Driver"
        assert transport.cost == 75.0

    def test_init_with_zero_cost(self):
        transport = Transportation("Bus", "Driver", 0.0)
        assert transport.cost == 0.0
        assert transport.passengers == []

    def test_init_with_negative_cost(self):
        transport = Transportation("Car", "Driver", -10.0)
        assert transport.cost == -10.0

    def test_add_passenger_valid_non_vip(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        guest = Guest("Regular Guest", "G001", False)
        transport.add_passenger(guest)
        assert len(transport.passengers) == 1
        assert transport.passengers[0] == guest
        assert transport.cost == 50.0

    def test_add_passenger_valid_vip(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        guest = Guest("VIP Guest", "G002", True)
        transport.add_passenger(guest)
        assert len(transport.passengers) == 1
        assert transport.passengers[0] == guest
        assert transport.cost == 55.0

    def test_add_passenger_vip_increases_cost(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        guest = Guest("VIP Guest", "G002", True)
        initial_cost = transport.cost
        transport.add_passenger(guest)
        assert transport.cost == initial_cost + 5

    def test_add_multiple_passengers_non_vip(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        g1 = Guest("Guest 1", "G001", False)
        g2 = Guest("Guest 2", "G002", False)
        g3 = Guest("Guest 3", "G003", False)
        transport.add_passenger(g1)
        transport.add_passenger(g2)
        transport.add_passenger(g3)
        assert len(transport.passengers) == 3
        assert transport.cost == 50.0

    def test_add_multiple_passengers_all_vip(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        g1 = Guest("VIP 1", "G001", True)
        g2 = Guest("VIP 2", "G002", True)
        g3 = Guest("VIP 3", "G003", True)
        transport.add_passenger(g1)
        transport.add_passenger(g2)
        transport.add_passenger(g3)
        assert len(transport.passengers) == 3
        assert transport.cost == 65.0

    def test_add_multiple_passengers_mixed(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        g1 = Guest("Regular", "G001", False)
        g2 = Guest("VIP", "G002", True)
        g3 = Guest("Regular", "G003", False)
        g4 = Guest("VIP", "G004", True)
        transport.add_passenger(g1)
        transport.add_passenger(g2)
        transport.add_passenger(g3)
        transport.add_passenger(g4)
        assert len(transport.passengers) == 4
        assert transport.cost == 60.0

    def test_add_passenger_invalid_type(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        with pytest.raises(ValueError, match="Invalid Guest."):
            transport.add_passenger("not a guest")

    def test_add_passenger_none(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        with pytest.raises(ValueError, match="Invalid Guest."):
            transport.add_passenger(None)

    def test_add_passenger_invalid_object(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        with pytest.raises(ValueError, match="Invalid Guest."):
            transport.add_passenger({"name": "Guest"})

    def test_add_same_passenger_multiple_times(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        guest = Guest("VIP Guest", "G001", True)
        transport.add_passenger(guest)
        transport.add_passenger(guest)
        assert len(transport.passengers) == 2
        assert transport.cost == 60.0

    def test_passenger_count_empty(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        assert transport.passenger_count() == 0

    def test_passenger_count_single(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        guest = Guest("Guest", "G001", False)
        transport.add_passenger(guest)
        assert transport.passenger_count() == 1

    def test_passenger_count_multiple(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        g1 = Guest("Guest 1", "G001", False)
        g2 = Guest("Guest 2", "G002", False)
        g3 = Guest("Guest 3", "G003", False)
        transport.add_passenger(g1)
        transport.add_passenger(g2)
        transport.add_passenger(g3)
        assert transport.passenger_count() == 3

    def test_passenger_count_consistency(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        assert transport.passenger_count() == len(transport.passengers)
        guest = Guest("Guest", "G001", False)
        transport.add_passenger(guest)
        assert transport.passenger_count() == len(transport.passengers)

    def test_empty_string_parameters(self):
        transport = Transportation("", "", 0.0)
        assert transport.vehicle == ""
        assert transport.driver == ""
        assert transport.cost == 0.0

    def test_vip_cost_increment_with_zero_initial_cost(self):
        transport = Transportation("Sedan", "John Driver", 0.0)
        guest = Guest("VIP Guest", "G001", True)
        transport.add_passenger(guest)
        assert transport.cost == 5.0

    def test_vip_cost_increment_with_negative_initial_cost(self):
        transport = Transportation("Sedan", "John Driver", -10.0)
        guest = Guest("VIP Guest", "G001", True)
        transport.add_passenger(guest)
        assert transport.cost == -5.0

    def test_add_passengers_preserves_order(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        g1 = Guest("Guest 1", "G001", False)
        g2 = Guest("Guest 2", "G002", False)
        g3 = Guest("Guest 3", "G003", False)
        transport.add_passenger(g1)
        transport.add_passenger(g2)
        transport.add_passenger(g3)
        assert transport.passengers[0] == g1
        assert transport.passengers[1] == g2
        assert transport.passengers[2] == g3

    def test_cost_calculation_with_many_vips(self):
        transport = Transportation("Bus", "Driver", 100.0)
        for i in range(10):
            guest = Guest(f"VIP {i}", f"G{i}", True)
            transport.add_passenger(guest)
        assert transport.cost == 150.0
        assert transport.passenger_count() == 10

    def test_cost_calculation_precision(self):
        transport = Transportation("Sedan", "Driver", 50.5)
        guest = Guest("VIP", "G001", True)
        transport.add_passenger(guest)
        assert transport.cost == 55.5

    def test_add_passenger_vip_status_check(self):
        transport = Transportation("Sedan", "John Driver", 50.0)
        regular = Guest("Regular", "G001", False)
        vip = Guest("VIP", "G002", True)
        transport.add_passenger(regular)
        cost_after_regular = transport.cost
        transport.add_passenger(vip)
        cost_after_vip = transport.cost
        assert cost_after_regular == 50.0
        assert cost_after_vip == 55.0

    def test_multiple_transports_same_guest(self):
        transport1 = Transportation("Sedan", "Driver 1", 50.0)
        transport2 = Transportation("SUV", "Driver 2", 75.0)
        guest = Guest("VIP Guest", "G001", True)
        transport1.add_passenger(guest)
        transport2.add_passenger(guest)
        assert transport1.passenger_count() == 1
        assert transport2.passenger_count() == 1
        assert transport1.cost == 55.0
        assert transport2.cost == 80.0

    def test_large_number_of_passengers(self):
        transport = Transportation("Bus", "Driver", 100.0)
        for i in range(50):
            is_vip = i % 2 == 0
            guest = Guest(f"Guest {i}", f"G{i}", is_vip)
            transport.add_passenger(guest)
        assert transport.passenger_count() == 50
        expected_cost = 100.0 + (25 * 5)
        assert transport.cost == expected_cost
