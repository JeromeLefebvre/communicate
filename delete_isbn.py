
import sys
from store import redis

isbns = [line.rstrip() for line in sys.argv[1:]]

for isbn in isbns:
	a = redis.get(isbn)
	b = redis.srem("books",a)
	if b != True:
		raise ValueError(isbn + " might not be in the table")
