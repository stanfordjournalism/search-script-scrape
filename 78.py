# Number of Cupertino, CA restaurants that have been shut down due to health violations in the last six months.
import requests
from lxml import html
url = 'https://services.sccgov.org/facilityinspection/Closure/Index?sortField=sortbyEDate'
doc = html.fromstring(requests.get(url).text)
print(len([t for t in doc.cssselect('td') if 'CUPERTINO' in t.text_content()]))
