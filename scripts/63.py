# In the current dataset behind Medicare's Nursing Home Compare website, the total amount of fines received by penalized nursing homes
# landing page:
# https://data.medicare.gov/data/nursing-home-compare
import csv
import os
import requests
from lxml import html
from shutil import unpack_archive
from urllib.parse import urljoin, urlparse, parse_qs
LOCAL_DATADIR = "/tmp/nursinghomes"
CSV_NAME = os.path.join(LOCAL_DATADIR, 'Penalties_Download.csv')
os.makedirs(LOCAL_DATADIR, exist_ok = True)
#
# The zip URL looks like this:
#  https://data.medicare.gov/views/bg9k-emty/files/AsD4-xSfJuwZKwb_gMosljIKMST...
#  TZ1PmBSoRGqivFmo?filename=DMG_CSV_DOWNLOAD20150501.zip&content_type=application%2Fzip%3B%20charset%3Dbinary

# we assume that the zip file URL changes frequently and can't be hardcoded
# so we go through the process of auto-magically determining that URL
url = 'https://data.medicare.gov/data/nursing-home-compare'
doc = html.fromstring(requests.get(url).text)
zipurl = [a.attrib['href'] for a in doc.cssselect('a')
                        if 'CSV_DOWNLOAD' in str(a.attrib.get('href'))][0]
zipurl = urljoin(url, zipurl)
bname = parse_qs(urlparse(zipurl).query)['filename'][0]
zname = os.path.join(LOCAL_DATADIR, bname)
if not os.path.exists(zname):
    print("Downloading", zipurl, 'to', zname)
    z = requests.get(zipurl).content
    with open(zname, 'wb') as f:
        f.write(z)
print('Unzipping', zname, 'to', LOCAL_DATADIR)
unpack_archive(zname, LOCAL_DATADIR)
rows = list(csv.DictReader(open(CSV_NAME, encoding = 'ISO-8859-1')))
print(sum([float(r['fine_amt']) for r in rows if r['fine_amt']]))
