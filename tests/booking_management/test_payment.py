import pytest
from booking_management.Payment import Payment
from booking_management.Invoice import Invoice


class TestPayment:
    def test_init(self):
        payment = Payment("PAY001", 100.0, "credit_card")
        assert payment.payment_id == "PAY001"
        assert payment.amount == 100.0
        assert payment.method == "credit_card"
        assert payment.invoice is None

    def test_attach_invoice_valid(self):
        payment = Payment("PAY001", 100.0, "credit_card")
        invoice = Invoice("INV001", 150.0, "USD")
        payment.attach_invoice(invoice)
        assert payment.invoice == invoice

    def test_attach_invoice_invalid_type(self):
        payment = Payment("PAY001", 100.0, "credit_card")
        with pytest.raises(ValueError, match="Invalid invoice"):
            payment.attach_invoice("not an invoice")

    def test_attach_invoice_reduces_amount(self):
        payment = Payment("PAY001", 200.0, "credit_card")
        invoice = Invoice("INV001", 150.0, "USD")
        payment.attach_invoice(invoice)
        assert payment.amount == 150.0

    def test_attach_invoice_amount_already_lower(self):
        payment = Payment("PAY001", 50.0, "credit_card")
        invoice = Invoice("INV001", 150.0, "USD")
        payment.attach_invoice(invoice)
        assert payment.amount == 50.0

    def test_process_success(self):
        payment = Payment("PAY001", 100.0, "credit_card")
        result = payment.process()
        assert result is True
        assert payment.amount == 97.0

    def test_process_with_fees(self):
        payment = Payment("PAY001", 1000.0, "credit_card")
        payment.process()
        assert payment.amount == 970.0

    def test_process_zero_amount(self):
        payment = Payment("PAY001", 0.0, "credit_card")
        result = payment.process()
        assert result is False

    def test_process_negative_amount(self):
        payment = Payment("PAY001", -50.0, "credit_card")
        result = payment.process()
        assert result is False

    def test_process_small_amount(self):
        payment = Payment("PAY001", 1.0, "credit_card")
        result = payment.process()
        assert result is True
        assert payment.amount == 0.97

    def test_process_multiple_times(self):
        payment = Payment("PAY001", 100.0, "credit_card")
        payment.process()
        first_amount = payment.amount
        payment.process()
        assert payment.amount < first_amount
