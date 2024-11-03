class Invoice:
    """Generates an invoice for a given order."""
    
    def __init__(self, order):
        self.order = order

    def generate_invoice(self):
        # Creating a formatted invoice string
        invoice_details = "==============================\n"
        invoice_details += "            INVOICE           \n"
        invoice_details += "==============================\n"
        invoice_details += f"Customer: {self.order.customer.name}\n"
        invoice_details += "--------------------------------\n"
        invoice_details += "Items Purchased:\n"
        
        # Listing each item with its details
        for item in self.order.shopping_cart.items:
            invoice_details += f" - {item}\n"
        
        invoice_details += "--------------------------------\n"
        invoice_details += f"Total Price (including VAT): ${self.order.total_price:.2f}\n"
        invoice_details += "==============================\n"

        return invoice_details

    def __str__(self):
        return f"Invoice for order with total: ${self.order.total_price:.2f}"
