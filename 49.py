# Number of sponsored bills by Rep. Nancy Pelosi that were vetoed by the President
from lxml import html
import requests
import re
url = 'https://www.congress.gov/member/nancy-pelosi/P000197'
atts = {'q': '{"sponsorship":"sponsored","bill-status":"veto"}'}
doc = html.fromstring(requests.get(url, params = atts).text)
t = doc.cssselect('.results-number')[0].text_content()
# e.g. 1-25 of 4,897
r = re.search('(?<=of) *[\d,]+', t).group().replace(',', '').strip()
print(r)
