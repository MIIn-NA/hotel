from booking_management.Invoice import Invoice
class FinancialReport:
    def __init__(self, period: str, total_revenue: float, currency: str):
        self.period = period
        self.total_revenue = total_revenue
        self.currency = currency
        self.invoices: list[Invoice] = []

    def add_invoice(self, invoice: Invoice) -> None:
        if not isinstance(invoice, Invoice):
            raise ValueError("Invalid Invoice.")
        self.invoices.append(invoice)
        self.total_revenue += invoice.amount

    def summary(self) -> str:
        return f"{self.period}: {len(self.invoices)} invoices, {self.total_revenue} {self.currency}"
