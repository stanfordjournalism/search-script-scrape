# The number of OSHA enforcement inspections involving Wal-Mart in California since 2014
from lxml import html
import requests
import re
url = "https://www.osha.gov/pls/imis/establishment.search"
atts = {'Office': 'all',
 'State': 'CA',
 'endday': '13',
 'endmonth': '06',
 'endyear': '2015',
 'establishment': 'Wal-Mart',
 'officetype': 'all',
 'p_case': 'all',
 'p_violations_exist': 'all',
 'startday': '01',
 'startmonth': '01',
 'startyear': '2014'}

doc = html.fromstring(requests.get(url, params = atts).text)
# Looks like:
# <div class="text-right">
# Results 1 - 8 of 8
# </div>
v = re.search('of (\d+)', doc.cssselect('.text-right')[1].text)
print(int(v.groups()[0]))
