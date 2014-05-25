import requests

# Based on the info from https://openlibrary.org/dev/docs/api/covers
def isbn_to_saved_image(isbn):
    def cover_urls(isbn):
        return ["http://covers.openlibrary.org/b/isbn/" + isbn + '-' + size + ".jpg" for size in ['L', 'M', 'S']][0]

    url = cover_urls(isbn)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open('covers/' + isbn + '.jpg', 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
    else:
        raise ValueError("Didn't get the ok to save the image " + isbn)
