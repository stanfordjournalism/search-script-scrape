# The number of roll call votes that were rejected by a margin of less than 5 votes, in the first session of the U.S. Senate in the 114th Congress
# Note: this example shows how to scrape the Senate webpage, which is
# the WRONG thing to do in practice. Use the XML instead:
# http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.xml
# via https://twitter.com/octonion/status/611296541941321731
from lxml import html
import requests
import re
congress_num = 114
session_num = 1
url = ('http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_%s_%s.htm'
         % (congress_num, session_num))

doc = html.fromstring(requests.get(url).text)
# unnecessarily convoluted xpath statement, which I do here
# just so I can practice xpath statements
# http://stackoverflow.com/questions/1457638/xpath-get-nodes-where-child-node-contains-an-attribute
xstr = "//*[@id='contentArea']//table/tr[td[2][contains(text(), 'Rejected')]]"
# i.e. find all tr elements that have a 2nd td child with text that contains "Rejected"
xcount = 0
for r in doc.xpath(xstr):
    yeas, nays = re.search('(\d+)-(\d+)', r.find('td').text_content()).groups()
    if (int(nays) - int(yeas) < 5):
        xcount += 1

print(xcount)
