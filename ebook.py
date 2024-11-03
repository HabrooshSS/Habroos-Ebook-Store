class EBook:
    """Represents an e-book with title, author, publication date, genre, and price."""
    def __init__(self, title, author, publication_date, genre, price):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.price = price

    def __str__(self):
        return f"EBook(title={self.title}, author={self.author}, genre={self.genre}, price={self.price})"

