# The latest estimated population percent change for Detroit, MI, according to the latest Census QuickFacts summary.
import requests
from lxml import html
url = 'http://quickfacts.census.gov/qfd/states/26/2622000.html'
doc = html.fromstring(requests.get(url).text)
# this is sloppy but quick
col = doc.xpath('//td[contains(text(), "Population, percent change")]/following-sibling::td')[0]
print(col.text_content())
