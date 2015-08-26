# In fiscal year 2013, the short description of the most frequently cited type of FDA's inspectional observations related to food products.
from collections import Counter
from lxml import html
from urllib.parse import urljoin
from xlrd import open_workbook
import requests
import tempfile
LANDING_PAGE_URL = 'http://www.fda.gov/ICECI/Inspections/ucm250720.htm'
# The hardcoded URL for the Excel file is:
# http://www.fda.gov/downloads/ICECI/Inspections/UCM381532.xls
# But we'll programatically find it
doc = html.fromstring(requests.get(LANDING_PAGE_URL).text)
# HTML looks like:
# <a href="/downloads/ICECI/Inspections/UCM381532.xls" id="anch_47">
#    <linktitle>FY 2013 Excel File</linktitle>&nbsp;(XLS - 691KB)
# </a>

# i love xpath
hrefs = doc.xpath("//a[linktitle[contains(text(), '2013')] and contains(@href, 'xls')]//@href")
url = urljoin(LANDING_PAGE_URL, hrefs[0])
# eh just make a temp file
t = tempfile.TemporaryFile()
t.write(requests.get(url).content)
t.seek(0)
wb = open_workbook(file_contents=t.read())
# Each category has its own name, we need to find "Foods"
sheet = wb.sheet_by_name('Foods')
# find the column that contains "Short Description"
col_idx = next(idx for idx, txt in enumerate(sheet.row_values(0)) if "Short Description" == txt)
c = Counter(sheet.row_values(r)[col_idx] for r in range(sheet.nrows))
print(""""%s" for %s observations""" % c.most_common(1)[0])

