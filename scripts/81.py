# The latest release date for T-100 Domestic Market (U.S. Carriers) statistics report
from lxml import html
from datetime import datetime
import requests
LANDING_PAGE_URL = 'http://www.transtats.bts.gov/releaseinfo.asp'
doc = html.fromstring(requests.get(LANDING_PAGE_URL).text)
a = doc.xpath("//a[contains(text(), 'T-100 Domestic Market  (U.S. Carriers)')]")[0]
tr = a.getparent().getparent()
txt = tr.xpath("./td[3]/text()")[0] # e.g. ['8/13/2015:']
# messy
dt = datetime.strptime(txt, '%m/%d/%Y:')
print(dt.strftime("%Y-%m-%d"))
# 2015-08-13
