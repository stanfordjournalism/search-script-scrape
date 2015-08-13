# The total number of notices published on the most recent date to the Federal Register
import requests
from lxml import html
url = 'https://www.federalregister.gov/'
doc = html.fromstring(requests.get(url).text)
print(doc.cssselect('ul.statistics li a span')[0].text_content())
