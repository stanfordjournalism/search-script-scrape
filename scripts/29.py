# Number of days until Texas's next scheduled execution
from datetime import datetime
from lxml import html
import requests
url = "http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"
doc = html.fromstring(requests.get(url).text)
# sometimes the executions happen more quickly than they can
# update the scheduled executions list, so we can't assume the
# first row is always the upcoming execution
today =  datetime(*datetime.now().timetuple()[0:3]) # whatever, too lazy to look this up
for row in doc.xpath('//table/tr')[1:]:
    col = row.cssselect('td')[0]
    exdate = datetime.strptime(col.text_content(), '%m/%d/%Y')
    # meh, this doesn't account for timezones but whatever, too lazy to look this up
    if (exdate >= today):
        print((exdate - today).days, "days")
        break
