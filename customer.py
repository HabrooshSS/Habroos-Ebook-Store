from shoppingcart import ShoppingCart  # Import ShoppingCart

class Customer:
    """Represents a customer in the e-book store."""
    
    def __init__(self, name, contact_info, loyalty_member=False):
        self.name = name
        self.contact_info = contact_info
        self.loyalty_member = loyalty_member
        self.shopping_cart = ShoppingCart()  # Initialize an empty shopping cart

    def __str__(self):
        return f"Customer(name={self.name}, contact_info={self.contact_info}, loyalty_member={self.loyalty_member})"
