
import sys

from isbn_to_redis import store_to_redis

isbns = [line.rstrip() for line in sys.argv[1:]]

store_to_redis(isbns)