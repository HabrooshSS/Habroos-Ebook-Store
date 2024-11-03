from ebook import EBook
from customer import Customer
from shoppingcart import ShoppingCart
from Order import Order
from Invoice import Invoice

class Main:
    """Main class to demonstrate the functionalities of the E-Book Store system."""
    def __init__(self):
        self.customers = []
        self.catalog = []

    def add_customer(self, name, contact_info):
        customer = Customer(name, contact_info)
        self.customers.append(customer)
        return customer

    def add_ebook_to_catalog(self, title, author, publication_date, genre, price):
        ebook = EBook(title, author, publication_date, genre, price)
        self.catalog.append(ebook)
        return ebook

    def place_order(self, customer):
        order = Order(customer, customer.get_shopping_cart())
        invoice = Invoice(order)
        print(invoice.generate_invoice())

    def show_catalog(self):
        for ebook in self.catalog:
            print(ebook)

    def show_customers(self):
        for customer in self.customers:
            print(customer)


# Example Test Cases
def test_ebook_store_system():
    # Initialize Main class
    main = Main()

    # Add e-books to catalog
    print("Adding e-books to catalog...")
    ebook1 = main.add_ebook_to_catalog("Python Basics", "Habroosh", "2022", "Programming", 10.0)
    ebook2 = main.add_ebook_to_catalog("Deep Learning", "Saeed", "2023", "AI", 15.0)
    ebook3 = main.add_ebook_to_catalog("Data Science Essentials", "Suwaidi", "2021", "Data Science", 20.0)
    ebook4 = main.add_ebook_to_catalog("Blockchain Basics", "Jamal suwaidi", "2023", "Blockchain", 25.0)
    ebook5 = main.add_ebook_to_catalog("Cybersecurity 101", "Mohammad jamal", "2020", "Security", 30.0)

    # Display catalog
    print("\nCatalog:")
    main.show_catalog()

    # Add a customer
    print("\nAdding a customer...")
    customer1 = main.add_customer("Habroosh Al Suwaidi", "habroosh2002@gmail.com")
    customer1.loyalty_member = True 

    # Add e-books to customer's shopping cart
    print("\nAdding e-books to shopping cart...")
    customer1.get_shopping_cart().add_item(ebook1)
    customer1.get_shopping_cart().add_item(ebook2)
    customer1.get_shopping_cart().add_item(ebook3)


    # Display the customer and cart
    print("\nCustomer Details:")
    print(customer1)
    print("\nShopping Cart:")
    print(customer1.get_shopping_cart())

    # Place an order and generate an invoice
    print("\nPlacing an order and generating invoice:")
    main.place_order(customer1)

    # Test for bulk discount (5 or more items)
    print("\nAdding more items to cart for bulk discount test...")
    customer1.get_shopping_cart().add_item(ebook4)
    customer1.get_shopping_cart().add_item(ebook5)


    # Place another order and generate an invoice
    print("\nPlacing a bulk order and generating invoice with bulk discount:")
    main.place_order(customer1)


# Run the test cases
if __name__ == "__main__":
    test_ebook_store_system()
