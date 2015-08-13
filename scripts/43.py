# The number of citations that resulted from FDA inspections in fiscal year 2012
import requests
import csv
# list of citations is here:
# http://www.fda.gov/ICECI/Inspections/ucm346077.htm
csv_url = 'http://www.fda.gov/downloads/ICECI/Inspections/UCM346093.csv'
print("Downloading", csv_url)
resp = requests.get(csv_url)
rows = list(csv.DictReader(resp.text.splitlines()[2:]))
print(len(rows))
