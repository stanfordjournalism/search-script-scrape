# The total number of inmates executed by Florida since 1976
import requests
from lxml import html
url = "http://www.dc.state.fl.us/oth/deathrow/execlist.html"

doc = html.fromstring(requests.get(url).text)
tables = doc.cssselect('table.dcCSStableLight')
rows = tables[0].cssselect('tr')
# the first row is just the header row
print(len(rows) - 1)
