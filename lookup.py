import amazonproduct
from lxml import etree
from Book import Book

api = amazonproduct.API(locale='us')
def amazon_lookup(isbn, scaling = 0.25):
	items = api.call(Operation='ItemLookup',SearchIndex='Books',IdType='ISBN',ItemId=isbn, ResponseGroup='ItemAttributes')

	if len(items) > 1:
		print(isbn)
		raise ValueError("More than one such element")
	item = items[0]
	name = item.find('.//aws:Title', namespaces={'aws': "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}).text
	price = item.find('.//aws:FormattedPrice', namespaces={'aws': "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}).text
	price = str(int(float(price.lstrip('$'))*scaling)) + '$'
	try:
		author = item.find('.//aws:Author', namespaces={'aws': "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}).text
	except AttributeError:
		author = ""
	amazon_url = item.find('.//aws:DetailPageURL', namespaces={'aws': "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}).text
	return Book(name, price, isbn, author, amazon_url)

