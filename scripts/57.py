# The top 3 auto manufacturers, ranked by total number of recalls via NHTSA safety-related defect and compliance campaigns since 1967.
import csv
import requests

from collections import Counter
from io import BytesIO, TextIOWrapper
from zipfile import ZipFile

ZIP_URL = 'http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip'
# Schema comes from http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt
MFGNAME_FIELD_NUM = 7
counter = Counter()
print("Downloading", ZIP_URL)
resp = requests.get(ZIP_URL)
with ZipFile(BytesIO(resp.content)) as zfile:
    fname = zfile.filelist[0].filename
    print("Unzipping...", fname) # note: the unpacked zip is 120MB+
    with zfile.open(fname, 'rU') as zf:
        reader = csv.reader(TextIOWrapper(zf, encoding = 'latin-1'), delimiter = "\t")
        counter.update(row[MFGNAME_FIELD_NUM] for row in reader)

for mfgname, count in counter.most_common(3):
    print("%s: %s" % (mfgname, count))

