# For all of 2013, the number of potential signals of serious risks or new safety information that resulted from the FDA's FAERS
import requests
from urllib.parse import urljoin
from lxml import html
url = 'http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082196.htm'
doc = html.fromstring(requests.get(url).text)
links = [a.attrib['href'] for a in doc.cssselect('li a') if '2013' in a.text_content()]
x = 0
for href in links:
    u = urljoin(url, href)
    d = html.fromstring(requests.get(u).text)
    els = d.cssselect("#content .middle-column table tr")[1:]
    x += len(els)
print(x)
