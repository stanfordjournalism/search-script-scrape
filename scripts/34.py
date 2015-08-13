# In the latest FDA Weekly Enforcement Report, the number of Class I and Class II recalls involving food
import requests
from lxml import html
url = 'http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm'
doc = html.fromstring(requests.get(url).text)
reporturl = doc.xpath('//a[contains(text(), "Enforcement Report for ")]/@href')[0]
# example weekly report:
# http://www.accessdata.fda.gov/scripts/enforcement/enforce_rpt-Product-Tabs.cfm?action=Expand+Index&w=06102015&lang=eng
report = html.fromstring(requests.get(reporturl).text)
print(len(report.cssselect('tr.Food')))
