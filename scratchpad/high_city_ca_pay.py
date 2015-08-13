# The top 100 California city employees by per-capita total wages
# Modification to scripts/100.py
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
employees = [r for r in csv.DictReader(rows[4:])]
for employee in sorted(employees, key = foosalary, reverse = True)[0:100]: # show top 100
    print("%s in %s: $%s" % (employee['Position'], employee['Entity Name'], int(foosalary(employee))))
# If you're a fan of True Detective Season 2, the output ring a bell:
# http://www.latimes.com/local/california/la-me-vernon-true-detective-20150619-story.html
#
#
# Fire Chief in Vernon: $3312
# Director Of Light & Power in Vernon: $2318
# Chief Deputy City Attorney in Vernon: $1905
# Engineering Manager in Vernon: $1783
# Finance Director in Vernon: $1737
# Police Chief in Vernon: $1693
# Captain in Vernon: $1648
# Director Of Community Services in Vernon: $1630
# Battalion Chief in Vernon: $1589
# Director Health & Environmental Control in Vernon: $1583
# Battalion Chief in Vernon: $1556
# Battalion Chief in Vernon: $1552
# Battalion Chief in Vernon: $1527
# Assistant To The City Administrator in Vernon: $1450
# Electric Resource Planning & Development Manager in Vernon: $1446
# Fire Marshall in Vernon: $1445
# Engineer in Vernon: $1440
# Engineer in Vernon: $1427
# Captain in Vernon: $1400
# Engineer in Vernon: $1393
# Captain in Vernon: $1373
# Lieutenant in Vernon: $1356
# Captain in Vernon: $1333
# Police Officer in Vernon: $1318
# Captain in Vernon: $1315
# Resource Scheduler in Vernon: $1311
# Captain in Vernon: $1308
# Captain in Vernon: $1308
# Lieutenant in Vernon: $1305
# Captain in Vernon: $1302
# Lieutenant in Vernon: $1301
# Captain in Vernon: $1301
# Captain in Vernon: $1296
# Engineer in Vernon: $1291
# Captain in Vernon: $1286
# Captain in Vernon: $1283
# Captain in Vernon: $1281
# Sergeants in Vernon: $1259
# Captain in Vernon: $1253
# Captain in Vernon: $1238
# Lieutenant in Vernon: $1238
# Captain in Vernon: $1220
# Sergeants in Vernon: $1200
# Sergeants in Vernon: $1199
# Administrative Captain in Vernon: $1186
# Engineer in Vernon: $1180
# Sergeants in Vernon: $1177
# Engineer in Vernon: $1176
# Captain in Vernon: $1162
# Sergeants in Vernon: $1157
# Engineer in Vernon: $1150
# Sergeants in Vernon: $1139
# Police Officer in Vernon: $1129
# Engineer in Vernon: $1104
# Engineer in Vernon: $1091
# Engineer in Vernon: $1091
# Engineer in Vernon: $1074
# Firefighter in Vernon: $1073
# Director Of Business Service & Personnel in Vernon: $1068
# Firefighter in Vernon: $1066
# Engineer in Vernon: $1059
# Police Officer in Vernon: $1058
# Engineer in Vernon: $1051
# Sergeants in Vernon: $1051
# Assistant Finance Director in Vernon: $1048
# Supervising Electrical Engineer in Vernon: $1044
# Engineer in Vernon: $1044
# Resource Scheduler in Vernon: $1044
# Senior Electrical Inspector in Vernon: $1043
# Gas Systems Lead in Vernon: $1036
# Engineer in Vernon: $1036
# Police Officer in Vernon: $1026
# Operations Supervisor in Vernon: $1023
# Senior Electronics Technician in Vernon: $1019
# Police Officer in Vernon: $1014
# Engineer in Vernon: $1011
# Police Officer in Vernon: $1010
# Firefighter in Vernon: $999
# Police Officer in Vernon: $992
# Police Officer in Vernon: $991
# Public Works Superintendent in Vernon: $984
# Firefighter/Paramedic in Vernon: $984
# Utilities Compliance Officer in Vernon: $983
# Firefighter in Vernon: $981
# Firefighter/Paramedic in Vernon: $978
# It Manager in Vernon: $977
# Firefighter in Vernon: $977
# Firefighter/Paramedic in Vernon: $970
# Firefighter/Paramedic in Vernon: $969
# Firefighter in Vernon: $967
# Engineer in Vernon: $964
# Engineer in Vernon: $962
# Operations Manager in Vernon: $957
# Firefighter in Vernon: $954
# Police Officer in Vernon: $951
# Engineer in Vernon: $951
# Plan Checker in Vernon: $948
# Electric Dispatcher in Vernon: $947
# Police Officer in Vernon: $946
# Police Officer in Vernon: $944

