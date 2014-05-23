
import sys

print(sys.argv[1])

from Book import Book
from lookup import amazon_lookup
from store import redis

isbns = [line.rstrip() for line in sys.argv[1:]]

for isbn in isbns:
	book = amazon_lookup(isbn)
	redis.sadd("books", book.to_string())

