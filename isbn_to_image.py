import urllib
import json

isbn = '0387960368'

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