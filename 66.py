# The highest minimum wage as mandated by state law.
import requests
import re
from lxml import html
# helper foo
def foo(c):
    m = re.search('([A-Z]{2}).+?(\d+\.\d+)', c.text_content())
    if m:
        state, wage = m.groups()
        return (float(wage), state)
    else:
        return None

url = 'http://www.dol.gov/whd/minwage/america.htm'
doc = html.fromstring(requests.get(url).text)

# easiest target is "Consolidated State Minimum Wage Update Table",
#  of which the first column is: "Greater than federal MW"

# Love this elegant solution: find the text node, then search upwards with ancestor::
# http://stackoverflow.com/a/3923863/160863
xstr = "//text()[contains(., 'Greater than federal MW')]/ancestor::table[1]//tr/td[1]"
cols = [foo(c) for c in doc.xpath(xstr) if foo(c)]
topcol = max(cols)

print(topcol[1], topcol[0])
# DC 9.5

