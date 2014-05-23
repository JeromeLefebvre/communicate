
from Book import Book
from store import redis

def allBooks():
	books = []
	for entry in redis.smembers("books"):
		books.append(Book.from_string(entry))
	return books

if __name__ == "__main__":
	print(allBooks())