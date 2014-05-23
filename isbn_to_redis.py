from Book import Book
from lookup import amazon_lookup
from store import redis

isbns = [line.rstrip() for line in open("isbn_db.txt")]

for isbn in isbns:
	book = amazon_lookup(isbn)
	redis.sadd("books", book.to_string())
