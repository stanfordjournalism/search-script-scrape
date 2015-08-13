# Number of days until Texas's next scheduled execution
from datetime import datetime
from lxml import html
import requests
# get next execution
url = "http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"
doc = html.fromstring(requests.get(url).text)
col = doc.xpath('//table/tr[2]/td[1]')[0]
exdate = datetime.strptime(col.text_content(), '%m/%d/%Y')

print((exdate - datetime.now()).days)
