# The difference in total White House staffmember salaries in 2014 versus 2010
import csv
import requests
# info https://www.whitehouse.gov/briefing-room/disclosures/annual-records/2014
url2010 = 'https://open.whitehouse.gov/api/views/rcp4-3y7g/rows.csv?accessType=DOWNLOAD'
url2014 = 'https://open.whitehouse.gov/api/views/i9g8-9web/rows.csv?accessType=DOWNLOAD'

d2010 = list(csv.DictReader(requests.get(url2010).text.splitlines()))
d2014 = list(csv.DictReader(requests.get(url2014).text.splitlines()))

s2010 = 0
for d in d2010:
    s2010 += float(d['Salary'].replace('$', ''))

s2014 = 0
for d in d2014:
    s2014 += float(d['Salary'].replace('$', ''))

print(s2014 - s2010)
