
from store import redis

books = redis.smembers("books")

for book in books:
	title, price, isbn, author, url = book.decode('utf-8').split(':::')
	print(isbn)