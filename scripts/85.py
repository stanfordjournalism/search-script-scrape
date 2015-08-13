# The number of iPhone units sold in the latest quarter, according to Apple Inc's most recent 10-Q report
# This exercise is just mean...The intent is to lead students to SEC's EDGAR,
#   *not* to imply that scraping EDGAR is the ideal way to do this fact-finding
import requests
from lxml import html
from urllib.parse import urljoin
# The target URL looks like this:
# http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=10-Q&owner=exclude&count=40
BASE_URL = 'http://www.sec.gov/cgi-bin/browse-edgar'
AAPL_CIK = "0000320193"
url_params = {
    'CIK': AAPL_CIK,
    'action': 'getcompany',
    'type': '10-Q',
    'owner':'exclude',
    'count': 40}
# do initial search for Apple's 10-Q forms
resp = requests.get(BASE_URL, params = url_params)
doc = html.fromstring(resp.text)
hrefs = doc.xpath("//a[@id='documentsbutton']/@href")
xurl = urljoin(BASE_URL, hrefs[0])
# fetch page for most recent 10-Q:
xdoc = html.fromstring(requests.get(xurl).text)
# this gets us a list of more documents. Select the URL
# for the one with 10q in its name
href10q = xdoc.xpath("//table[@class='tableFile']//a[contains(@href, '10q.htm')]/@href")[0]
url10q = urljoin(BASE_URL, href10q)
# one more request
qdoc = html.fromstring(requests.get(url10q).text)
# now for some truly convoluted parsing logic
# First, an xpath trick: http://stackoverflow.com/questions/1457638/xpath-get-nodes-where-child-node-contains-an-attribute
xtd = qdoc.xpath("//td[descendant::p[contains(text(), 'Unit Sales by Product:')]]")[0]
# luckily there's only one such <td>.
# Data looks like this:
# | 3 months |         |         |        | (9 months) |         |      |
# |   Unit   | June 27 | June 28 |        |            |         |      |
# |  sales   |   2015  |   2015  | Change |            |         |      |
# |----------|---------|---------|--------|------------|---------|------|
# | iPhone   | 47,534  | 35,203  | 35%    | 183,172    | 129,947 | 41%  |
# | iPad     | 10,931  | 13,276  | -18%   | 44,973     | 55,661  | -19% |
# | Mac      | 4,796   | 4,413   | 9%     | 14,878     | 13,386  | 11%  |

xtr = xtd.getparent() # i.e. the enclosing tr...we need to move to the next tr
# find the first row that has "iPhone" in it
iphone_row = next(tr for tr in xtr.itersiblings() if 'iPhone' in tr.text_content())
# fourth column has the data, as cols 2 and 3 are padding:
sales = int(iphone_row.xpath('td[@align="right"][1]/text()')[0].replace(',', ''))
print(sales * 1000) # units are listed in thousands
# 47534000 (for June 2015)
