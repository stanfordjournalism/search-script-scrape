# The sum of White House staffermember salaries in 2014
# Note: this is a pretty verbose step-by-step
import requests
import csv
url = "https://open.whitehouse.gov/api/views/i9g8-9web/rows.csv?accessType=DOWNLOAD"
txt = requests.get(url).text
# save the file temporarily
f = open("/tmp/salaries2014.csv", "w")
f.write(txt)
f.close()
###
# reopen (yes, this is wasteful, but whatever)
f = open("/tmp/salaries2014.csv", "r")
rows = list(csv.DictReader(f))
totes = 0
for r in rows:
    # remove $ sign, convert to float
    salval = float(r['Salary'].replace('$', ''))
    totes += salval

print(totes)

