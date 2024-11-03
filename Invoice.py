class Invoice:
    """Generates an invoice for a given order."""
    def __init__(self, order):
        self.order = order

    def generate_invoice(self):
        invoice_details = f"Customer: {self.order.customer.name}\n"
        invoice_details += f"Items: {[str(item) for item in self.order.shopping_cart.items]}\n"
        invoice_details += f"Total Price (including VAT): ${self.order.total_price:.2f}"
        return invoice_details

    def __str__(self):
        return f"Invoice for order with total ${self.order.total_price:.2f}"
