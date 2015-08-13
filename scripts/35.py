# Most viewed data set on New York state's open data portal as of this month
import requests
from lxml import html
# There's probably a JSON endpoint for this...but what the heck, let's
# do HTML parsing
url = 'https://data.ny.gov/browse?sortBy=most_accessed&sortPeriod=month'
doc = html.fromstring(requests.get(url).text)
t = doc.cssselect('tr.item .titleLine a')[0]
print(t.text_content())
