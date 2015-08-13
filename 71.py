# The percent increase in number of babies named Archer nationwide in 2010 compared to 2000, according to the Social Security Administration
# landing page:
# http://www.ssa.gov/oact/babynames/limits.html
import csv
import os
import requests
from shutil import unpack_archive

LOCAL_DATADIR = "/tmp/babynames"
os.makedirs(LOCAL_DATADIR, exist_ok = True)
url = 'http://www.ssa.gov/oact/babynames/names.zip'
zname = os.path.join(LOCAL_DATADIR, 'names.zip')
# download the file
if not os.path.exists(zname):
    print("Downloading", url, 'to', zname)
    z = requests.get(url).content
    with open(zname, 'wb') as f:
        f.write(z)
# Unzip the data
print('Unzipping', zname, 'to', LOCAL_DATADIR)
unpack_archive(zname, LOCAL_DATADIR)
d = {2010: 0, 2000: 0}
for y in d.keys():
    fname = os.path.join(LOCAL_DATADIR, "yob%d.txt" % y)
    rows = list(csv.reader(open(fname)))
    # each row looks like this:
    # Pamela,F,258
    d[y] += sum([int(r[2]) for r in rows if r[0] == 'Archer'])

print(100 * (d[2010] - d[2000]) / d[2000])


