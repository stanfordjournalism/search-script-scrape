# In 2010, the year-over-year change in enplanements at America's busiest airport
# The landing page for this data is:
# http://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger/
# For each year, there's a separate page with a table of links, including
# XLS format:
# e.g. ./passenger/media/cy10_primary_enplanements.xls
import csv
import requests
# we can't be sure that the XLS has the same naming convention year over year
#  so let's do a little HTML parsing
from lxml import html
from os.path import basename
from urllib.parse import urljoin
from xlrd import open_workbook

BASE_URL = "http://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger/"
YEAR = 2010
resp = requests.get(BASE_URL, params = {'year': YEAR})
doc = html.fromstring(resp.text)
# There are several spreadsheets and conventions over the years. I'm going to
#  be lazy and just pick the first spreadsheet with "enplanements" and assume it's the primary
#  doc
xls_url = doc.xpath("//a[contains(@href, 'enplanements') and contains(@href, 'xls')]/@href")[0]
print("Downloading", xls_url)
xresp = requests.get(urljoin(BASE_URL, xls_url))
# save to disk
fn = "/tmp/" + basename(xls_url)
with open(fn, "wb") as f:
    f.write(xresp.content)
# open with xlrd
book = open_workbook(fn)
sheet = book.sheets()[0]
# Format looks like this:
# |                  Airport                   |    CY 10     |    CY 09     |
# |                    Name                    | Enplanements | Enplanements |
# |--------------------------------------------|--------------|--------------|
# | Hartsfield - Jackson Atlanta International | 43,130,585   | 42,280,868   |
# | Chicago O'Hare International               | 32,171,831   | 31,135,732   |
# | Los Angeles International                  | 28,857,755   | 27,439,897   |

headers = sheet.row_values(0)
# get all the data rows
rows = [sheet.row_values(i) for i in range(1, sheet.nrows)]
# make them into dicts
drows = [dict(zip(headers, row)) for row in rows]
# remove rows without 'CY 10 Enplanements' as a float
drows = [d for d in drows if isinstance(d['CY 10 Enplanements'], float)]
# get biggest airport
airport = max(drows, key = lambda r: r['CY 10 Enplanements'])
print("%s: %i" % (airport['Airport Name'], airport['CY 10 Enplanements'] - airport['CY 09 Enplanements']))
# Hartsfield - Jackson Atlanta International: 849717
