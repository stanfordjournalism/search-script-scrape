# How much did the state of California collect in property taxes, according to the U.S. Census 2013 Annual Survey of State Government Tax Collections?
# landing page: http://www.census.gov/govs/statetax/historical_data.html
# note: this exercise was one of the last to be done and is done in the most just-do-everything-in-one-line mode possible
# ...don't actually follow it as good practice
import requests
from io import BytesIO
from xlrd import open_workbook
from zipfile import ZipFile
ZIP_URL = 'http://www2.census.gov/govs/statetax/state_tax_collections.zip'
XLS_FNAME = 'STC_Historical_DB.xls'
print("Downloading:", ZIP_URL)
resp = requests.get(ZIP_URL)
with ZipFile(BytesIO(resp.content)) as zfile:
    with open("/tmp/state_tax_data.xls", "wb") as o:
        o.write(zfile.open(XLS_FNAME, 'r').read())
book = open_workbook("/tmp/state_tax_data.xls")
sheet = book.sheets()[0]
# T01 refers to "Property Tax", get the index
proptax_col_idx = next(idx for idx, c in enumerate(sheet.row_values(1)) if 'T01' in c)
# state name is in column indexed 2
# note that each state has more than one row, but the first one is the most recent
cal_row = next(sheet.row_values(x) for x in range(sheet.nrows) if 'CA STATE' in sheet.row_values(x)[2])
print("%s paid %s in the year %s" % (cal_row[2], cal_row[proptax_col_idx] * 1000, round(cal_row[0])))
