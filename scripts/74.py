# The description of the bill most recently signed into law by the governor of Georgia
from lxml import html
import requests
import re
url = 'https://gov.georgia.gov/bills-signed'
txt = requests.get(url).text
hrefs = re.findall('(?<=/bills-signed/)\d{4}', txt)
yrurl = url + '/' + max(hrefs)
# e.g. https://gov.georgia.gov/bills-signed/2015
doc = html.fromstring(requests.get(yrurl).text)
# most recent bill is at the top
print(doc.xpath('//tr/td[2]/a')[0].text_content())
