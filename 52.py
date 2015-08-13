# The average wage of optometrists according to the BLS's most recent National Occupational Employment and Wage Estimates report
from lxml import html
import requests
url = 'http://www.bls.gov/oes/current/oes_nat.htm'
doc = html.fromstring(requests.get(url).text)
table = doc.cssselect('#bodytext table')[0]
t = next(tr for tr in table.cssselect('tr') if 'Optometrists' in tr.text_content())
print( t.cssselect('td')[-2].text_content())
