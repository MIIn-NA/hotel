import pytest
from services.Order import Order
from user_management.Guest import Guest


class TestOrder:
    def test_init(self):
        order = Order("ORD001", 150.0, "pending")
        assert order.order_id == "ORD001"
        assert order.total == 150.0
        assert order.status == "pending"
        assert order.guest is None

    def test_init_with_different_values(self):
        order = Order("ORD002", 250.50, "confirmed")
        assert order.order_id == "ORD002"
        assert order.total == 250.50
        assert order.status == "confirmed"

    def test_init_with_zero_total(self):
        order = Order("ORD003", 0.0, "pending")
        assert order.total == 0.0
        assert order.guest is None

    def test_init_with_negative_total(self):
        order = Order("ORD004", -50.0, "pending")
        assert order.total == -50.0

    def test_assign_guest_valid_non_vip(self):
        order = Order("ORD001", 100.0, "pending")
        guest = Guest("John Doe", "G001", False)
        order.assign_guest(guest)
        assert order.guest == guest
        assert order.total == 100.0

    def test_assign_guest_valid_vip(self):
        order = Order("ORD001", 100.0, "pending")
        guest = Guest("Jane Smith", "G002", True)
        order.assign_guest(guest)
        assert order.guest == guest
        assert order.total == 90.0

    def test_assign_guest_vip_discount_calculation(self):
        order = Order("ORD001", 200.0, "pending")
        guest = Guest("VIP Guest", "G003", True)
        order.assign_guest(guest)
        assert order.total == 180.0

    def test_assign_guest_vip_discount_precision(self):
        order = Order("ORD001", 150.75, "pending")
        guest = Guest("VIP Guest", "G003", True)
        order.assign_guest(guest)
        expected = 150.75 * 0.9
        assert order.total == pytest.approx(expected, rel=1e-9)

    def test_assign_guest_invalid_type(self):
        order = Order("ORD001", 100.0, "pending")
        with pytest.raises(ValueError, match="Invalid Guest."):
            order.assign_guest("not a guest")

    def test_assign_guest_none(self):
        order = Order("ORD001", 100.0, "pending")
        with pytest.raises(ValueError, match="Invalid Guest."):
            order.assign_guest(None)

    def test_assign_guest_invalid_object(self):
        order = Order("ORD001", 100.0, "pending")
        with pytest.raises(ValueError, match="Invalid Guest."):
            order.assign_guest({"name": "John"})

    def test_assign_guest_multiple_times_non_vip(self):
        order = Order("ORD001", 100.0, "pending")
        guest1 = Guest("John Doe", "G001", False)
        guest2 = Guest("Jane Smith", "G002", False)
        order.assign_guest(guest1)
        order.assign_guest(guest2)
        assert order.guest == guest2
        assert order.total == 100.0

    def test_assign_guest_multiple_times_vip(self):
        order = Order("ORD001", 100.0, "pending")
        guest1 = Guest("VIP1", "G001", True)
        guest2 = Guest("VIP2", "G002", True)
        order.assign_guest(guest1)
        assert order.total == 90.0
        order.assign_guest(guest2)
        assert order.total == 81.0

    def test_assign_guest_vip_with_zero_total(self):
        order = Order("ORD001", 0.0, "pending")
        guest = Guest("VIP Guest", "G001", True)
        order.assign_guest(guest)
        assert order.total == 0.0

    def test_update_status_valid(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("confirmed")
        assert order.status == "CONFIRMED"

    def test_update_status_uppercase_conversion(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("processing")
        assert order.status == "PROCESSING"

    def test_update_status_mixed_case(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("CoNfIrMeD")
        assert order.status == "CONFIRMED"

    def test_update_status_strips_whitespace(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("  confirmed  ")
        assert order.status == "CONFIRMED"

    def test_update_status_with_leading_whitespace(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("   delivered")
        assert order.status == "DELIVERED"

    def test_update_status_with_trailing_whitespace(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("cancelled   ")
        assert order.status == "CANCELLED"

    def test_update_status_too_short(self):
        order = Order("ORD001", 100.0, "pending")
        with pytest.raises(ValueError, match="Status too short."):
            order.update_status("AB")

    def test_update_status_two_characters(self):
        order = Order("ORD001", 100.0, "pending")
        with pytest.raises(ValueError, match="Status too short."):
            order.update_status("OK")

    def test_update_status_empty_string(self):
        order = Order("ORD001", 100.0, "pending")
        with pytest.raises(ValueError, match="Status too short."):
            order.update_status("")

    def test_update_status_whitespace_only(self):
        order = Order("ORD001", 100.0, "pending")
        with pytest.raises(ValueError, match="Status too short."):
            order.update_status("   ")

    def test_update_status_exactly_three_characters(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("NEW")
        assert order.status == "NEW"

    def test_update_status_three_chars_with_whitespace(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("  NEW  ")
        assert order.status == "NEW"

    def test_update_status_two_chars_after_strip(self):
        order = Order("ORD001", 100.0, "pending")
        with pytest.raises(ValueError, match="Status too short."):
            order.update_status("  AB  ")

    def test_update_status_multiple_times(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("confirmed")
        assert order.status == "CONFIRMED"
        order.update_status("processing")
        assert order.status == "PROCESSING"
        order.update_status("delivered")
        assert order.status == "DELIVERED"

    def test_empty_string_parameters(self):
        order = Order("", 0.0, "")
        assert order.order_id == ""
        assert order.total == 0.0
        assert order.status == ""

    def test_assign_guest_then_update_status(self):
        order = Order("ORD001", 100.0, "pending")
        guest = Guest("VIP Guest", "G001", True)
        order.assign_guest(guest)
        assert order.total == 90.0
        order.update_status("confirmed")
        assert order.status == "CONFIRMED"
        assert order.total == 90.0

    def test_update_status_then_assign_guest(self):
        order = Order("ORD001", 100.0, "pending")
        order.update_status("confirmed")
        guest = Guest("VIP Guest", "G001", True)
        order.assign_guest(guest)
        assert order.status == "CONFIRMED"
        assert order.total == 90.0

    def test_assign_non_vip_then_vip_guest(self):
        order = Order("ORD001", 100.0, "pending")
        non_vip = Guest("Regular", "G001", False)
        vip = Guest("VIP", "G002", True)
        order.assign_guest(non_vip)
        assert order.total == 100.0
        order.assign_guest(vip)
        assert order.total == 90.0

    def test_vip_discount_on_negative_total(self):
        order = Order("ORD001", -100.0, "pending")
        guest = Guest("VIP Guest", "G001", True)
        order.assign_guest(guest)
        assert order.total == -90.0

    def test_large_total_vip_discount(self):
        order = Order("ORD001", 10000.0, "pending")
        guest = Guest("VIP Guest", "G001", True)
        order.assign_guest(guest)
        assert order.total == 9000.0
