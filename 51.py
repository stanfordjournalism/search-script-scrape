# The title of the most recent decision handed down by the U.S. Supreme Court
import requests
from lxml import html
url = 'http://www.supremecourt.gov/opinions/slipopinions.aspx'
doc = html.fromstring(requests.get(url).text)
print(doc.cssselect("#mainbody table tr a")[0].text_content())
