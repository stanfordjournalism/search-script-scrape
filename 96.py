# The number of scheduled arguments according to the most recent U.S. Supreme Court argument calendar
from lxml import html
from urllib.parse import urljoin
import requests
url = 'http://www.supremecourt.gov/oral_arguments/argument_calendars.aspx'
index = html.fromstring(requests.get(url).text)
# calendar is sorted chronologically, with latest in the last link
href = index.xpath('//a[contains(text(), "HTML")]/@href')[-1]
cal = html.fromstring(requests.get(urljoin(url, href)).text)
pdfs = cal.xpath("//table//a[contains(@href, 'qp.pdf')]/@href")
print(len(pdfs))
