import requests

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

'''
Initial try using a google database, did not work out in the end
import urllib
import json

json_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn

json_document = urllib.urlopen(json_url)

json_text = ''.join(json_document.readlines())

j = json.loads(json_text)

print(j["items"][0]["volumeInfo"])
print([l["imageLinks"] for l in j["items"][0]["volumeInfo"].values()])

#extracts = [p["extract"] for p in json["query"]["pages"].values()]

thumbnail_url = j["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]

print(thumbnail_url)
#urllib.urlretrieve(thumbnail_url, "cover/" + isbn + ".png")
'''