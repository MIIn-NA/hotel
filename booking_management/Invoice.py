class Invoice:
    def __init__(self, invoice_id: str, total: float, currency: str):
        self.invoice_id = invoice_id
        self.total = total
        self.currency = currency

    def apply_tax(self, percent: float) -> None:
        if percent < 0:
            raise ValueError("Tax cannot be negative.")
        tax_value = self.total * (percent / 100)
        self.total += tax_value
        self.total = round(self.total, 2)

    def convert_currency(self, rate: float) -> float:
        if rate <= 0:
            raise ValueError("Invalid conversion rate.")
        converted = self.total * rate
        return round(converted, 2)
