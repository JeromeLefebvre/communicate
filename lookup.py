import amazonproduct
from lxml import etree

api = amazonproduct.API(locale='us')
items = api.call(Operation='ItemLookup',SearchIndex='Books',IdType='ISBN',ItemId='9780521375108', ResponseGroup='ItemAttributes')
#items = api.item_lookup('9780521375108', IdType='ISBN', SearchIndex='Books', )
#items = api.item_lookup('052137510X', IdType='ISBN', SearchIndex='Books')
for item in items:
	print(etree.tostring(item, pretty_print=True))
	#print(type(item))
item = items[0]
#print(etree.tostring(item, pretty_print=True))


print(item.find('.//aws:FormattedPrice', namespaces={'aws': "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}).text)

print(item.find('.//aws:Author', namespaces={'aws': "http://webservices.amazon.com/AWSECommerceService/2011-08-01"}).text)

#q = etree.fromstring(etree.tostring(item, pretty_print=True))

#q = etree.fromstring('<xml><ItemLookupResponse><manufacturer>Doubleday</manufacturer></ItemLookupResponse></xml>')

#print(q.findall(".//FormattedPrice"))

#q = etree.fromstring('<xml><hello>a</hello><x><hello>b</hello></x></xml>')

#print(q.findall('.//hello')[0].text)