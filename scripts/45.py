# The number of security alerts issued by US-CERT in the current year
import requests
from lxml import html
url = 'https://www.us-cert.gov/ncas/alerts'
doc = html.fromstring(requests.get(url).text)
print(len(doc.cssselect('.item-list li')))
