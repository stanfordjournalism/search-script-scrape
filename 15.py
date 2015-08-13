# Total number of wildlife strike incidents reported at San Francisco International Airport
# landing page
# http://wildlife.faa.gov/database.aspx
import csv
import os
import requests
from shutil import unpack_archive
from subprocess import check_output
AIRPORTCODE = 'KSFO'
LOCAL_DATADIR = "/tmp/faawildlife"
url = 'http://wildlife.faa.gov/downloads/wildlife.zip'
zname = os.path.join(LOCAL_DATADIR, os.path.basename(url))
dname = os.path.join(LOCAL_DATADIR, 'wildlife.accdb')
os.makedirs(LOCAL_DATADIR, exist_ok = True)

# Download the zip
if not os.path.exists(zname):
    print("Downloading", url, 'to', zname)
    z = requests.get(url).content
    with open(zname, 'wb') as f:
        f.write(z)

# unzip it
print("Unzipping", zname, 'to', LOCAL_DATADIR)
unpack_archive(zname, LOCAL_DATADIR)

# Work with MS Access, using mdbtools
# https://github.com/brianb/mdbtools
#
# Install with:
#   brew install mdbtools
# Helpful post:
#   http://nialldonegan.me/2007/03/10/converting-microsoft-access-mdb-into-csv-or-mysql-in-linux/

# $ mdb-tables wildlife.accdb
# STRIKE_REPORTS (1990-1999) STRIKE_REPORTS (2000-2009) STRIKE_REPORTS (2010-Current) STRIKE_REPORTS_BASH (1990-Current)
# hardcode the tablenames
access_tablenames = ['STRIKE_REPORTS (1990-1999)', 'STRIKE_REPORTS (2000-2009)', 'STRIKE_REPORTS (2010-Current)', 'STRIKE_REPORTS_BASH (1990-Current)']
hitcount = 0
for tname in access_tablenames:
    txt = check_output("mdb-export %s '%s'" % (dname, tname), shell = True).decode()
    rows = list(csv.DictReader(txt.splitlines()))
    hits = len([r for r in rows if r['AIRPORT_ID'] == AIRPORTCODE])
    print(tname, " - ", hits)
    hitcount += hits

print("Total:")
print(hitcount)
