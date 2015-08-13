# Number of stop-and-frisk reports from the NYPD in 2014
from shutil import unpack_archive
import csv
import os
import requests
DATADIR = '/tmp/nypd'
os.makedirs(DATADIR, exist_ok = True)
zipurl = 'http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/2014_sqf_csv.zip'
zname = os.path.join(DATADIR, os.path.basename(zipurl))
cname = os.path.join(DATADIR, '2014.csv')
if not os.path.exists(zname):
    print("Downloading", zipurl, 'to', zname)
    z = requests.get(zipurl).content
    with open(zname, 'wb') as f:
        f.write(z)
# unzip it
unpack_archive(zname, DATADIR)

data = list(csv.DictReader(open(cname, encoding = 'latin-1')))
print(len(data))


