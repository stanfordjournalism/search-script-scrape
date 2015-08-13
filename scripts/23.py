# The name of the California school with the highest number of girls enrolled in kindergarten, according to the CA Dept. of Education's latest enrollment data file.
import csv
import requests
from collections import defaultdict
from operator import itemgetter
url = 'http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2014-15&cCat=Enrollment&cPage=filesenr.asp'

def foo(row):
    return int(row['KDGN']) if row['KDGN'] else 0

lines = requests.get(url).text.splitlines()
data = list(csv.DictReader(lines, delimiter = "\t"))

codes = defaultdict(int)
for d in data:
    if d['GENDER'] == 'F':
        codes[d['CDS_CODE']] += int(d['KDGN'])

cds, num = max(codes.items(), key = itemgetter(1))
print([d['SCHOOL'] for d in data if d['CDS_CODE'] == cds][0])

