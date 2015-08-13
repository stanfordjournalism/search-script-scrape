import requests
from lxml import html
url = "http://www.state.gov/secretary/travel/index.htm"
resp = requests.get(url)
x = html.fromstring(resp.text).cssselect('#total-mileage span')
print(x[0].text_content())
