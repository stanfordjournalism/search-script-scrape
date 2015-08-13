# The highest salary possible for a White House staffmember in 2014
import csv
import requests
url = 'https://open.whitehouse.gov/api/views/i9g8-9web/rows.csv?accessType=DOWNLOAD'
data = list(csv.DictReader(requests.get(url).text.splitlines()))

def foo(d):
    return float(d['Salary'].replace('$', ''))

print(max(data, key = foo)['Salary'])
