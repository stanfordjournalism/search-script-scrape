# According to the Medill National Security Zone, the number of chambered guns confiscated at airports by the TSA in 2014
# http://nationalsecurityzone.org
import csv
import requests
gdoc_url = 'https://docs.google.com/spreadsheets/d/1a65n2HIcBYG7VyZYfVnBXGDmEdR8NYSOF43dzkDIuwA/'
txt = requests.get(gdoc_url + 'export', params = {'format': 'csv', 'gid': 0}).text
# skip the first two lines, which are:
# Mandatory credit, with link: TSA data compiled by Medill National Security Journalism Initiative.
# Data is preliminary and extracted from the TSA Blog. TSA'S year-end totals may very slightly.
rows = list(csv.DictReader(txt.splitlines()[2:]))
print(len([r for r in rows if r['CHAMBERED?'] == 'Y']))
