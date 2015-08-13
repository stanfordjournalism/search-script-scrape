# The number of failed votes in the roll calls 1 through 99, in the U.S. House of the 114th Congress
import requests
from lxml import html
# There are many places to get roll call info, including the House Clerk:
# http://clerk.house.gov/evs/2015/index.asp
# We could programmatically find the target page but it's not
#   worth it for this exercise:
URL = 'http://clerk.house.gov/evs/2015/ROLL_000.asp'
doc = html.fromstring(requests.get(URL).text)
# good ol' Xpath
print(len(doc.xpath('//tr/td[5]/font[text()="F"]')))
# 28
