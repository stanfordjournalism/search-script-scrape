# Number of datasets currently listed on data.gov
from lxml import html
import requests
response = requests.get('http://www.data.gov/')
doc = html.fromstring(response.text)
link = doc.cssselect('small a')[0]
print(link.text)
