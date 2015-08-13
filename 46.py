# The number of Pinterest accounts maintained by U.S. State Department embassies and missions

# Note: You can extend this problem to include ALL Pinterest
# accounts (e.g. maintained by Consulates) because
# the HTML structure here is atrocious
import requests
from lxml import html
url = 'http://www.state.gov/r/pa/ode/socialmedia/'
doc = html.fromstring(requests.get(url).text)
pinlinks = [a for a in doc.cssselect('a') if 'pinterest.com' in str(a.attrib.get('href'))]
# we just need a count, so no need to do anything more
# sophisticated
print(len(pinlinks))
