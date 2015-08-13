# The number of workplace fatalities at reported to the federal and state OSHA in the latest fiscal year
# landing page
# https://www.osha.gov/dep/fatcat/dep_fatcat.html
from lxml import html
from urllib.parse import urljoin
import csv
import requests
url = "https://www.osha.gov/dep/fatcat/dep_fatcat.html"
doc = html.fromstring(requests.get(url).text)
links = [a.attrib['href'] for a in doc.cssselect('a') if a.attrib.get('href')]
# assume first CSV is the target csv
csvurl = urljoin(url, [a for a in links if 'csv' in a][0])
rows = list(csv.DictReader(requests.get(csvurl).text.splitlines()))
print(len([r for r in rows if r['Fatality or Catastrophe'] == 'Fatality']))
