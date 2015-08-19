# The dropout rate for all of Santa Clara County high schools, according to the latest cohort data in CALPADS
import csv
from urllib.request import urlopen
from io import TextIOWrapper as Tio
from lxml import html
COUNTY =  'Santa Clara'
# This problem actually requires two datasets:
# 1) The Dept. of Ed's list of county ID numbers to find Santa Clara
SCHOOL_DB_URL = 'ftp://ftp.cde.ca.gov/demo/schlname/pubschls.txt'
# 2) The latest cohort data file from CALPADS
CALPADS_PAGE_URL = "http://www.cde.ca.gov/ds/sd/sd/filescohort.asp"
# Obviously you could hardcode Santa Clara County's ID number but that
#  would be too easy. Doing a lookup of the ID let's us modify the script
#  to work with any county.
# ...unfortunately, CDE has the list of county IDs to be such boring info
#   that they don't put it an easy to find way. OK, so let's just download
#   their entire schools database just to get one number:
with urlopen(SCHOOL_DB_URL) as schoolsdb:
    print("Downloading", SCHOOL_DB_URL)
    txt = Tio(schoolsdb, encoding = 'latin-1')
    rows = csv.DictReader(txt, delimiter = '\t')
    county_id = next(r['CDSCode'][0:2] for r in rows if r['County'] == COUNTY)
    print(COUNTY, 'ID is:', county_id)
print("Downloading", CALPADS_PAGE_URL)
doc = html.fromstring(urlopen(CALPADS_PAGE_URL).read())
# um, I'm curious about howtheir ASP app here works...but whatever...
urls = doc.xpath("//a[contains(@href, 'dlfile.aspx?cLevel=All')]/@href")
# being lazy and assuming first item is the most recent
calpads_url = urls[0]
print("Downloading", calpads_url)
dropouts, total = 0, 0
with urlopen(calpads_url) as calpadsdb:
    print("Downloading", calpads_url)
    txt = Tio(calpadsdb, encoding = 'latin-1')
    for row in csv.DictReader(txt, delimiter = '\t'):
        # not every row is to be counted, as each school has a separate row
        #  for each subgroup. So the filter condition is not just by county
        #   but also by 'AggLevel' == 'S' and 'Subgroup' == 'All'
        if(row['CDS'][0:2] == county_id and row['AggLevel'] == 'S'
                                         and row['Subgroup'] == 'All'):
            try: # sooooo lazy...
                total += int(row['NumCohort'])
                dropouts += int(row['NumDropouts'])
            except:
                pass # not a number; some cells have '*'

print(dropouts / total)
# 0.09737916232841275
