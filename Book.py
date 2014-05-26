from collections import namedtuple

Book = namedtuple("book", ["title", "price", "isbn", "author"], verbose=False)

def to_string(self):
	return self.title + ":::" + self.price + ":::" + self.isbn + ":::" + self.author
Book.to_string = to_string

@staticmethod
def from_string(string):
	# everything stored in redis is a binary in python, thus for python 3 we must first convert it to a string\
	name, price, isbn, author = string.decode("utf-8").split(':::')
	return Book(str(name), price, isbn, author)
Book.from_string = from_string