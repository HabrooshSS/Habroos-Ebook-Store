class EBook:
    """Represents an e-book with title, author, publication date, genre, and price."""    
    def __init__(self, title, author, publication_date, genre, price):
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self.price = price 

    def get_title(self):
        """Returns the title of the e-book."""
        return self._title

    def set_title(self, title):
        """Sets the title of the e-book."""
        self._title = title

    def get_author(self):
        """Returns the author of the e-book."""
        return self._author

    def set_author(self, author):
        """Sets the author of the e-book."""
        self._author = author

    def get_publication_date(self):
        """Returns the publication date of the e-book."""
        return self._publication_date

    def set_publication_date(self, publication_date):
        """Sets the publication date of the e-book."""
        self._publication_date = publication_date

    def get_genre(self):
        """Returns the genre of the e-book."""
        return self._genre

    def set_genre(self, genre):
        """Sets the genre of the e-book."""
        self._genre = genre

    def get_price(self):
        """Returns the price of the e-book."""
        return self.price

    def set_price(self, price):
        """Sets the price of the e-book."""
        self.price = price

    def __str__(self):
        return f"EBook(title={self._title}, author={self._author}, genre={self._genre}, price={self.price})"
