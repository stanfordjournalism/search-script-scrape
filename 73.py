# The total amount of contributions made by lobbyists to Congress according to the latest downloadable quarterly report
from glob import glob
from lxml import etree, html
from shutil import unpack_archive
import os
import requests
DATADIR = '/tmp/lobbying'
os.makedirs(DATADIR, exist_ok = True)
url = 'http://www.senate.gov/legislative/Public_Disclosure/contributions_download.htm'
# get listing of databases
doc = html.fromstring(requests.get(url).text)
# assuming most recent file is at the top of the page
zipurl = sorted(doc.xpath('//a[contains(@href, "zip")]/@href'))[-1]
zname = os.path.join(DATADIR, os.path.basename(zipurl))
# Download the zip of the latest quarterly report
if not os.path.exists(zname):
    print("Downloading", zipurl, 'to', zname)
    z = requests.get(zipurl).content
    with open(zname, 'wb') as f:
        f.write(z)
# unzip it
print("Unzipping", zname, 'to', DATADIR)
unpack_archive(zname, DATADIR)

ctotal = 0
# each zip contains multiple xml files
for x in glob(os.path.join(DATADIR, '*.xml')):
    xtxt = '\n'.join(open(x, encoding = 'utf-16').readlines()[1:])
    xdoc = etree.fromstring(xtxt)
    ctotal += sum(float(c) for c in xdoc.xpath('//Contribution/@Amount'))

# note: this is a naive summation, without regard to whether each
# Contribution node is apples-to-apples, and if corrections are made later
print(ctotal)
