# The total number of preliminary reports on aircraft safety incidents/accidents in the last 10 business days
from lxml import html
import requests
url = 'http://www.asias.faa.gov/pls/apex/f?p=100:93:0::NO:::'
doc = html.fromstring(requests.get(url).text)
x = 0
for tr in doc.cssselect('#uPageCols tr')[2:3]:
    for t in tr.cssselect('td')[1:]:
        v = re.search('\d+', t.text_content())
        if v:
            x += int(v.group())
print(x)
