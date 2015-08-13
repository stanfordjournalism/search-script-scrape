# The names of the committees that Sen. Barbara Boxer currently serves on
import requests
from lxml import html
url="http://www.senate.gov/general/committee_assignments/assignments.htm"
doc = html.fromstring(requests.get(url).text)
row = next(tr for tr in doc.cssselect('tr') if 'Boxer, Barbara' in tr.text_content())
print(len(row.cssselect('td')[1].cssselect('a')))
