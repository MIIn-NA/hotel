import pytest
from booking_management.Invoice import Invoice


class TestInvoice:
    def test_init(self):
        invoice = Invoice("INV001", 100.0, "USD")
        assert invoice.invoice_id == "INV001"
        assert invoice.total == 100.0
        assert invoice.currency == "USD"

    def test_apply_tax_basic(self):
        invoice = Invoice("INV001", 100.0, "USD")
        invoice.apply_tax(10.0)
        assert invoice.total == 110.0

    def test_apply_tax_zero(self):
        invoice = Invoice("INV001", 100.0, "USD")
        invoice.apply_tax(0.0)
        assert invoice.total == 100.0

    def test_apply_tax_negative(self):
        invoice = Invoice("INV001", 100.0, "USD")
        with pytest.raises(ValueError, match="Tax cannot be negative"):
            invoice.apply_tax(-5.0)

    def test_apply_tax_rounding(self):
        invoice = Invoice("INV001", 99.99, "USD")
        invoice.apply_tax(15.5)
        assert invoice.total == 115.49

    def test_apply_tax_multiple_times(self):
        invoice = Invoice("INV001", 100.0, "USD")
        invoice.apply_tax(10.0)
        invoice.apply_tax(5.0)
        assert invoice.total == 115.5

    def test_convert_currency_basic(self):
        invoice = Invoice("INV001", 100.0, "USD")
        result = invoice.convert_currency(1.2)
        assert result == 120.0

    def test_convert_currency_zero_rate(self):
        invoice = Invoice("INV001", 100.0, "USD")
        with pytest.raises(ValueError, match="Invalid conversion rate"):
            invoice.convert_currency(0.0)

    def test_convert_currency_negative_rate(self):
        invoice = Invoice("INV001", 100.0, "USD")
        with pytest.raises(ValueError, match="Invalid conversion rate"):
            invoice.convert_currency(-1.5)

    def test_convert_currency_rounding(self):
        invoice = Invoice("INV001", 99.99, "USD")
        result = invoice.convert_currency(0.85)
        assert result == 84.99

    def test_convert_currency_doesnt_modify_total(self):
        invoice = Invoice("INV001", 100.0, "USD")
        invoice.convert_currency(1.5)
        assert invoice.total == 100.0

    def test_apply_tax_then_convert(self):
        invoice = Invoice("INV001", 100.0, "USD")
        invoice.apply_tax(20.0)
        result = invoice.convert_currency(0.9)
        assert result == 108.0
