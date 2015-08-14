# Number of days until Texas's next scheduled execution
from datetime import datetime
from lxml import html
import pytz
import requests
url = "http://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"
# fetch and parse the page
doc = html.fromstring(requests.get(url).text)
# Get our time in central texas time; http://stackoverflow.com/a/22109768/160863
texas_time = pytz.timezone("US/Central")
today = texas_time.localize(datetime(*datetime.now().timetuple()[0:3])) # whatever, too lazy to look up the idiom
for row in doc.xpath('//table/tr')[1:]:
    # Even though this table is sorted in reverse-chronological order,
    #  sometimes the executions happen more quickly than the updates to the
    #  webpage, can't assume the first row is always the upcoming execution
    #
    # Each row looks like:
    # | 08/12/2015 |  Info | Lopez | Daniel | 999555 | 09/15/1987 | H | 03/16/2010 | Nueces |
    col = row.cssselect('td')[0]
    exdate = datetime.strptime(col.text_content(), '%m/%d/%Y')
    exdate = texas_time.localize(exdate)
    if (exdate >= today):
        print((exdate - today).days, "days")
        break
