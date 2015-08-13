# The sum of White House staffermember salaries in 2014
import requests
import csv
url = "https://open.whitehouse.gov/api/views/i9g8-9web/rows.csv?accessType=DOWNLOAD"
txt = requests.get(url).text
totes = 0
for r in csv.DictReader(txt.splitlines()):
    # remove $ sign, convert to float
    salval = float(r['Salary'].replace('$', ''))
    totes += salval
print(totes)
# 37776925.0
