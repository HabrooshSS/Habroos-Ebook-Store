class Order:
    """Represents an order with an itemized list, applicable discounts, VAT, and final price."""
    VAT_RATE = 0.08

    def __init__(self, customer, shopping_cart):
        self.customer = customer
        self.shopping_cart = shopping_cart
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total = self.shopping_cart.get_total_price()
        discount = 0.2 if len(self.shopping_cart.items) >= 5 else 0.1 if self.customer.loyalty_member else 0
        total_after_discount = total * (1 - discount)
        return total_after_discount * (1 + Order.VAT_RATE)

    def __str__(self):
        return f"Order(total_price={self.total_price:.2f}, VAT={Order.VAT_RATE * 100}%)"