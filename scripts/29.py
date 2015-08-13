# Number of days until Texas's next scheduled execution

from datetime import datetime
from lxml import html
import requests
# get next execution
url = "http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"
doc = html.fromstring(requests.get(url).text)
# sometimes the executions happen more quickly
# than they can update the page so we can't assume the first row
# is always the upcoming execution
today =  datetime.now()
for row in doc.xpath('//table/tr')[1:]:
    col = row.cssselect('td')[0]
    exdate = datetime.strptime(col.text_content(), '%m/%d/%Y')
    # meh, whatever, too lazy to look up timezone information
    if exdate.strftime('%Y-%m-%d') >= today.strftime('%Y-%m-%d'):
        # if there's an execution today, the result will be -1
        print((exdate - datetime.now()).days)
        break
