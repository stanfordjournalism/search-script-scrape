# The California city whose city manager earns the most total wage per population of its city in 2012
import csv
import requests
from io import BytesIO
from zipfile import ZipFile
YEAR = 2012
def foosalary(row):
    tw = float(row['Total Wages']) if row['Total Wages'] else 0
    return tw / int(row['Entity Population'])

url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file=%s_City.zip' % YEAR
print("Downloading:", url)
resp = requests.get(url)
zfile = ZipFile(BytesIO(resp.content))
fname = zfile.filelist[0].filename # 2012_City.csv
rows = zfile.read(fname).decode('latin-1').splitlines()
# first 4 lines are Disclaimer lines
managers = [r for r in csv.DictReader(rows[4:]) if r['Position'].lower() == 'city manager']
topman = max(managers, key = foosalary)
print("City: %s; Pay-per-Capita: $%s" % (topman['Entity Name'], int(foosalary(topman))))
# City: Industry; Pay-per-Capita: $465

