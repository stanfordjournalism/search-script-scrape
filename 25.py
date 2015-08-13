# Average frontal crash star rating for 2015 Honda Accords
import requests
import re
from lxml import html

url = 'http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/2011-Newer+Vehicles/Search-Results'
atts = {"searchtype":"model", "make": "HONDA", "model": "ACCORD", "year": 2015}
doc = html.fromstring(requests.get(url, params = atts).text)
trs = doc.cssselect("#dataarea tr")
v = 0
for tr in trs[1:-1]:
    t = tr.cssselect('td.b_right img.stars')[1].attrib['alt']
    v += int(re.search('\d+', t).group())
print(v / len(trs[1:-1]))
