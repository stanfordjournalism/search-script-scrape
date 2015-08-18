# The New York City high school with the highest average math score in the latest SAT results

# Notes:
# As this is one of the last exercises that I've written out, it includes code
#  that is both lazy and unnecessarily elaborate. You can check out other
#  scraping/spreadsheet parsing examples to find cleaner ways of doing this.
#
# Landing page:
# http://schools.nyc.gov/Accountability/data/TestResults/default.htm
#
## Relevant text from the webpage:
# The most recent school level results for New York City on the SAT.
#  Results are available at the school level for the graduating
#  seniors of 2014.  For a summary report of SAT, PSAT, and AP achievement
#  for 2014, please click here.
#
## Target URL looks like this:
# http://schools.nyc.gov/NR/rdonlyres/CE9139F0-9F3A-4C42-ACB8-74F2D014802F/
#                                           171380/2014SATWebsite10214.xlsx
#
# It's just as likely that by next year, they'll redesign or restructure
#  the site. So this scraping code is unstable. But it works as of August 2015.
import requests
from io import BytesIO
from urllib.parse import urljoin
from lxml import html
from openpyxl import load_workbook
LANDING_PAGE_URL = 'http://schools.nyc.gov/Accountability/data/TestResults/default.htm'

doc = html.fromstring(requests.get(LANDING_PAGE_URL).text)
# instead of using xpath, let's just use a sloppy csscelect
urls = [a.attrib.get('href') for a in doc.cssselect('a')]
# that awkward `get` is because not all anchor tags have hrefs...and
#  this is why we use xpath...
_xurl = next(url for url in urls if url and 'SAT' in url and 'xls' in url) # blargh
xlsx_url = urljoin(LANDING_PAGE_URL, _xurl)
# download the spreadsheet...instead of writing to disk
# let's just keep it in memory and pass it directly to load_workbook()
xlsx = BytesIO(requests.get(xlsx_url).content)
wb = load_workbook(xlsx)
# The 2014 edition contains two worksheets, the first being "Notes"
#  and the second being "2014 SAT Results"
# Let's write an agnostic function as if we didn't know how each year's
#   spreadsheet was actually structured
sheet = next(s for s in wb.worksheets if "results" in s.title.lower())
