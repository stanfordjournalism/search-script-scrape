# Total number of clinical trials as recorded by the National Institutes of Health
import requests
from lxml import html
url = 'https://clinicaltrials.gov/'
doc = html.fromstring(requests.get(url).text)
e = doc.cssselect('#trial-count > p > .highlight')[0]
print(e.text_content())
