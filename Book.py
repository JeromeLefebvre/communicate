from collections import namedtuple

Book = namedtuple("book", ["title", "price", "isbn"], verbose=False)

def to_string(self):
	return self.title + ":::" + self.price + ":::" + self.isbn
Book.to_string = to_string

@staticmethod
def from_string(str):
	name, price, isbn = str.split(':::')
	return Book(name, price, isbn)
Book.from_string = from_string