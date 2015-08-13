# The number of people on FBI's Most Wanted List for white collar crimes
import requests
from lxml import html
url = 'http://www.fbi.gov/wanted/wcc/@@wanted-group-listing'
doc = html.fromstring(requests.get(url).text)
print(len(doc.cssselect('.contenttype-FBIPerson')))
