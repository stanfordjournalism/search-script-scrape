# The number of U.S. congressmembers who have Twitter accounts, according to Sunlight Foundation data
# info https://sunlightlabs.github.io/congress/#legislator-spreadsheet
import csv
import requests
url = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
rows = list(csv.DictReader(requests.get(url).text.splitlines()))
# note that spreadsheet includes non-sitting legislators, thus the use
# of 'in_office' attribute to filter
print(len([r for r in rows if r['twitter_id'] and r['in_office'] == '1']))
