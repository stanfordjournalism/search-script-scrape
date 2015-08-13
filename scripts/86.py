# Number of computer vulnerabilities in which IBM was the vendor in the latest Cyber Security Bulletin
import requests
from lxml import html
from urllib.parse import urljoin
url = 'https://www.us-cert.gov/ncas/bulletins'
doc = html.fromstring(requests.get(url).text)
href = doc.xpath('//*[@class="document_title"]/a/@href')[0]
bulletin = html.fromstring(requests.get(urljoin(url, href)).text)
trs = bulletin.xpath('//tr/td[1][contains(text(), "ibm")]')
print(len(trs))
