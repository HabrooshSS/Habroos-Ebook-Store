class ShoppingCart:
    """Represents a shopping cart containing e-books and handling cart operations."""
    def __init__(self):
        self.items = []

    def add_item(self, ebook):
        self.items.append(ebook)

    def remove_item(self, ebook):
        if ebook in self.items:
            self.items.remove(ebook)

    def get_total_price(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        return f"ShoppingCart(items={[str(item) for item in self.items]})"