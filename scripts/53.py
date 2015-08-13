# The total number of on-campus hate crimes as reported to the U.S. Office of Postsecondary Education, in the most recent collection year
# hardcode the url to 2014 file
# this task is just a mess, dependent on how well you can read
# documentation and deal with the messy arrangement of columns
from glob import glob
from shutil import unpack_archive
from xlrd import open_workbook
import os
import requests

LOCAL_FNAME = '/tmp/ope2014excel.zip'
LOCAL_DATADIR = "/tmp/ope2014excel"
url = 'http://ope.ed.gov/security/dataFiles/Crime2014EXCEL.zip'
# this is such a massive file that we should cache the download
if not os.path.exists(LOCAL_FNAME):
    print("Downloading", url, 'to', LOCAL_FNAME)
    with open(LOCAL_FNAME, 'wb') as f:
        f.write(requests.get(url).content)

# unzip
print("Unzipping", LOCAL_FNAME, 'to', LOCAL_DATADIR)
unpack_archive(LOCAL_FNAME, LOCAL_DATADIR, format = 'zip')
# get filename
fname = [f for f in glob(LOCAL_DATADIR + '/*.xlsx') if 'oncampushate' in f][0]
# open workbook
print("Opening", fname)
book = open_workbook(fname)
sheet = book.sheets()[0]
data = [sheet.row_values(i) for i in range(sheet.nrows)]
# get all column indices that correspond to relevant columns, i.e.
#
# 266 LAR_T_RAC13 Num 8           Larceny 2013 By Bias Race
# 267 LAR_T_REL13 Num 8           Larceny 2013 By Bias Religion
# 268 LAR_T_SEX13 Num 8           Larceny 2013 By Bias Sexual Orientation
# 269 LAR_T_GEN13 Num 8           Larceny 2013 By Bias Gender
# 270 LAR_T_DIS13 Num 8           Larceny 2013 By Bias Disability
# 271 LAR_T_ETH13 Num 8           Larceny 2013 By Bias Ethnicity
wanted_heds = ['RAC13', 'REL13', 'SEX13', 'GEN13', 'DIS13', 'ETH13']
indices = [i for i, c in enumerate(data[0]) if any(t in c for t in wanted_heds)]
crime_count = 0
for row in data[1:]:
    for i in indices:
        if row[i]:
            crime_count += int(row[i])
print(crime_count)
