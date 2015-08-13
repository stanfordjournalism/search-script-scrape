# Total number of officer-involved shooting incidents listed by the Philadelphia Police Department
import requests
from lxml import html
url = "https://www.phillypolice.com/ois/"
doc = html.fromstring(requests.get(url).text)
x = 0
for table in doc.cssselect('.ois-table'):
    x += len(table.cssselect('tr')) - 1
print(x)
