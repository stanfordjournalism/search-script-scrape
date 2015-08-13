# The number of international travel alerts from the U.S. State Department currently in effect
import requests
from lxml import html
url = 'http://travel.state.gov/content/passports/english/alertswarnings.html'
doc = html.fromstring(requests.get(url).text)
print(len(doc.cssselect('td.alert')))

