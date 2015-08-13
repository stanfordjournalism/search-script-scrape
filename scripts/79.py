#  The change in airline revenues from baggage fees, from 2013 to 2014
import requests
from lxml import html
# Note that the BTS provides CSV versions of each year
# So using HTML parsing is the dumb way to do this. oh well
BASE_URL = 'https://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/subject_areas/airline_information/baggage_fees/html/%s.html'
year_totes = {2013: 0, 2014: 0}

for yr in year_totes.keys():
    url = BASE_URL % yr
    resp = requests.get(url)
    doc = html.fromstring(resp.text)
    # Incredibly sloppy way of getting the total value from
    # the bottom-right cell of the table. oh well
    tval = doc.cssselect('tr td')[-1].text_content().strip()
    year_totes[yr] = int(tval.replace(',', '')) * 1000 # it's in 000s

print(year_totes[2014] - year_totes[2013])
# 179236000
