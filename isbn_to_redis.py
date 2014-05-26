from Book import Book
from lookup import amazon_lookup
from store import redis
from isbn_to_image import isbn_to_saved_image


def store_to_redis(isbns):
    for isbn in isbns:
        book = amazon_lookup(isbn)
        # Adding to the list of books
        redis.sadd("books", book.to_string())
        # so that the book data can be access later using the isbn
        redis.set(isbn, book.to_string())
        isbn_to_saved_image(isbn)
        with open("isbn_db.txt", "a") as myfile:
            myfile.write(isbn + "\n")

if __name__ == "__main__":
    isbns = [line.rstrip() for line in open("isbn_db.txt")]
    store_to_redis(isbns)
