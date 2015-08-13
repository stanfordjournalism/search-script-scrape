# In the "Justice News" RSS feed maintained by the Justice Department, the number of items published on a Friday
from datetime import datetime
from lxml import etree
import requests
url = 'http://www.justice.gov/feeds/opa/justice-news.xml'
doc = etree.fromstring(requests.get(url).content)
items = doc.xpath('//channel/item')
dates = [item.find('pubDate').text.strip() for item in items]
ts = [datetime.strptime(d.split(' ')[0], '%Y-%m-%d') for d in dates]
# for weekday(), 4 correspond to Friday
print(len([t for t in ts if t.weekday() == 4]))
