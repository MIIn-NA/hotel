from booking_management.Invoice import Invoice
class Payment:
    def __init__(self, payment_id: str, amount: float, method: str):
        self.payment_id = payment_id
        self.amount = amount
        self.method = method
        self.invoice: Invoice | None = None

    def attach_invoice(self, invoice: Invoice) -> None:
        if not isinstance(invoice, Invoice):
            raise ValueError("Invalid invoice.")
        self.invoice = invoice
        if invoice.total < self.amount:
            self.amount = invoice.total

    def process(self) -> bool:
        if self.amount <= 0:
            return False
        fees = self.amount * 0.03
        self.amount -= fees
        return self.amount > 0
