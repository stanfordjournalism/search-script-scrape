# The current humidity level at Great Smoky Mountains National Park
from lxml import html
import requests
url = "http://www.nature.nps.gov/air/WebCams/parks/grsmcam/grsmcam.cfm"
doc = html.fromstring(requests.get(url).text)
print(doc.cssselect('#CollapsiblePanel6 div div div')[3].text_content())
