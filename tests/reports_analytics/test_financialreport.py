import pytest
from reports_analytics.FinancialReport import FinancialReport
from booking_management.Invoice import Invoice


class TestFinancialReport:
    def test_init(self):
        report = FinancialReport("Q1 2024", 10000.0, "USD")
        assert report.period == "Q1 2024"
        assert report.total_revenue == 10000.0
        assert report.currency == "USD"
        assert report.invoices == []

    def test_init_with_zero_revenue(self):
        report = FinancialReport("Q2 2024", 0.0, "EUR")
        assert report.total_revenue == 0.0

    def test_init_with_negative_revenue(self):
        report = FinancialReport("Q3 2024", -5000.0, "GBP")
        assert report.total_revenue == -5000.0

    def test_init_invoices_list_empty(self):
        report = FinancialReport("Q1 2024", 1000.0, "USD")
        assert isinstance(report.invoices, list)
        assert len(report.invoices) == 0

    def test_add_invoice_valid(self):
        report = FinancialReport("Q1 2024", 0.0, "USD")
        invoice = Invoice("INV001", 500.0, "USD")
        invoice.amount = invoice.total  # Invoice uses 'total' but FinancialReport expects 'amount'
        report.add_invoice(invoice)
        assert len(report.invoices) == 1
        assert report.invoices[0] == invoice

    def test_add_invoice_increases_revenue(self):
        report = FinancialReport("Q1 2024", 1000.0, "USD")
        invoice = Invoice("INV001", 500.0, "USD")
        invoice.amount = invoice.total  # Invoice uses 'total' but FinancialReport expects 'amount'
        report.add_invoice(invoice)
        assert report.total_revenue == 1500.0

    def test_add_invoice_with_total_property(self):
        report = FinancialReport("Q1 2024", 0.0, "USD")
        invoice = Invoice("INV001", 250.0, "USD")
        invoice.amount = invoice.total  # Invoice uses 'total' but FinancialReport expects 'amount'
        report.add_invoice(invoice)
        assert report.total_revenue == 250.0

    def test_add_invoice_invalid_type(self):
        report = FinancialReport("Q1 2024", 0.0, "USD")
        with pytest.raises(ValueError, match="Invalid Invoice"):
            report.add_invoice("not an invoice")

    def test_add_invoice_invalid_type_dict(self):
        report = FinancialReport("Q1 2024", 0.0, "USD")
        with pytest.raises(ValueError, match="Invalid Invoice"):
            report.add_invoice({"invoice_id": "INV001"})

    def test_add_invoice_invalid_type_none(self):
        report = FinancialReport("Q1 2024", 0.0, "USD")
        with pytest.raises(ValueError, match="Invalid Invoice"):
            report.add_invoice(None)

    def test_add_multiple_invoices(self):
        report = FinancialReport("Q1 2024", 0.0, "USD")
        inv1 = Invoice("INV001", 100.0, "USD")
        inv1.amount = inv1.total
        inv2 = Invoice("INV002", 200.0, "USD")
        inv2.amount = inv2.total
        inv3 = Invoice("INV003", 300.0, "USD")
        inv3.amount = inv3.total
        report.add_invoice(inv1)
        report.add_invoice(inv2)
        report.add_invoice(inv3)
        assert len(report.invoices) == 3
        assert report.total_revenue == 600.0

    def test_summary(self):
        report = FinancialReport("Q1 2024", 1000.0, "USD")
        result = report.summary()
        assert result == "Q1 2024: 0 invoices, 1000.0 USD"

    def test_summary_with_invoices(self):
        report = FinancialReport("Q1 2024", 0.0, "USD")
        inv1 = Invoice("INV001", 100.0, "USD")
        inv1.amount = inv1.total
        inv2 = Invoice("INV002", 200.0, "USD")
        inv2.amount = inv2.total
        report.add_invoice(inv1)
        report.add_invoice(inv2)
        result = report.summary()
        assert result == "Q1 2024: 2 invoices, 300.0 USD"

    def test_summary_with_different_currency(self):
        report = FinancialReport("Q2 2024", 5000.0, "EUR")
        result = report.summary()
        assert result == "Q2 2024: 0 invoices, 5000.0 EUR"

    def test_summary_with_multiple_invoices(self):
        report = FinancialReport("Q3 2024", 0.0, "GBP")
        for i in range(5):
            invoice = Invoice(f"INV00{i}", 100.0, "GBP")
            invoice.amount = invoice.total
            report.add_invoice(invoice)
        result = report.summary()
        assert result == "Q3 2024: 5 invoices, 500.0 GBP"

    def test_summary_format(self):
        report = FinancialReport("January 2024", 1234.56, "USD")
        invoice = Invoice("INV001", 765.44, "USD")
        invoice.amount = invoice.total
        report.add_invoice(invoice)
        result = report.summary()
        assert "January 2024" in result
        assert "1 invoices" in result
        assert "2000.0 USD" in result

    def test_add_invoice_with_zero_amount(self):
        report = FinancialReport("Q1 2024", 100.0, "USD")
        invoice = Invoice("INV001", 0.0, "USD")
        invoice.amount = invoice.total
        report.add_invoice(invoice)
        assert report.total_revenue == 100.0

    def test_add_invoice_cumulative_revenue(self):
        report = FinancialReport("Q1 2024", 1000.0, "USD")
        initial_revenue = report.total_revenue
        invoice = Invoice("INV001", 500.0, "USD")
        invoice.amount = invoice.total
        report.add_invoice(invoice)
        assert report.total_revenue == initial_revenue + 500.0
