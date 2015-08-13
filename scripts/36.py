# Total number of visitors to the White House in 2012
# landing page:
# https://www.whitehouse.gov/briefing-room/disclosures/visitor-records
import csv
import os
import requests
from shutil import unpack_archive
LOCAL_DATADIR = "/tmp/whvisitors"
url = 'https://www.whitehouse.gov/sites/default/files/disclosures/whitehouse-waves-2012.csv_.zip'
zname = os.path.join(LOCAL_DATADIR, os.path.basename(url))
cname = os.path.join(LOCAL_DATADIR, 'WhiteHouse-WAVES-2012.csv')
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
# the file was zipped on a Mac, yet still uses Windows encoding...mkaaay
rows = list(csv.DictReader(open(cname, encoding = 'ISO-8859-1')))
print(len(rows))
# 934872
