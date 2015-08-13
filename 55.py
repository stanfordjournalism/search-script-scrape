# The number of Government Accountability Office reports and testimonies on the topic of veterans
import requests
import re
from lxml import html
url = 'http://www.gao.gov/browse/topic/Veterans'
doc = html.fromstring(requests.get(url).text)
txt = doc.cssselect('h2.scannableTitle')[0].text_content().strip()
# 'Veterans (1 - 10 of 1,170 items)'
v = re.search('of (\d+)', txt.replace(',', '')).groups()[0]
print(int(v))
