# Number of medical device recalls issued by the U.S. Food and Drug Administration in 2013
from lxml import html
import requests
url = 'http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm384618.htm'
doc = html.fromstring(requests.get(url).text)
print(len(doc.cssselect('tbody tr')))
