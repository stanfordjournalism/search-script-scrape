# The number of published research papers from the NSA
import requests
from lxml import html
url = 'https://www.nsa.gov/research/publications/index.shtml'
doc = html.fromstring(requests.get(url).text)
print(len(doc.cssselect('table.dataTable tr')[1:]))
