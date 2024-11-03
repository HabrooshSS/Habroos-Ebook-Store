from shoppingcart import ShoppingCart  # Import ShoppingCart

class Customer:
    """Represents a customer in the e-book store."""
    
    def __init__(self, name, contact_info, loyalty_member=False):
        self.name = name
        self._contact_info = contact_info
        self._loyalty_member = loyalty_member
        self._shoppingcart = ShoppingCart()  # Initialize an empty shopping cart

    def get_name(self):
        """Returns the name of the customer."""
        return self.name

    def set_name(self, name):
        """Sets the name of the customer."""
        self.name = name

    def get_contact_info(self):
        """Returns the contact information of the customer."""
        return self._contact_info

    def set_contact_info(self, contact_info):
        """Sets the contact information of the customer."""
        self._contact_info = contact_info

    def is_loyalty_member(self):
        """Returns whether the customer is a loyalty member."""
        return self._loyalty_member

    def set_loyalty_member(self, loyalty_member):
        """Sets the loyalty membership status of the customer."""
        self._loyalty_member = loyalty_member

    def get_shopping_cart(self):
        """Returns the customer's shopping cart."""
        return self._shoppingcart

    def __str__(self):
        return f"Customer(name={self.name}, contact_info={self._contact_info}, loyalty_member={self._loyalty_member})"
