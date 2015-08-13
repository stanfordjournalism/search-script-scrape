# The non-profit organization with the highest total revenue, according to the latest listing in ProPublica's Nonprofit Explorer
# Note: "latest listing" is kind of broad...we'll just take that to mean
#   top revenue of whatever's currently listed on the site
from lxml import html
import requests
url = 'https://projects.propublica.org/nonprofits/search?c_code%5Bid%5D=&ntee%5Bid%5D=&order=revenue&q=&sort_order=desc&state%5Bid%5D=&utf8=%E2%9C%93'
doc = html.fromstring(requests.get(url).text)
d = doc.xpath('//table/tbody/tr[1]/td/a/text()')
print(d[0])
# It's also possible to just use the API
# https://projects.propublica.org/nonprofits/api
