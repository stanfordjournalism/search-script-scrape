# The total number of babies named Odin born in Colorado according to the Social Security Administration
import shutil
import requests
url = 'http://www.ssa.gov/OACT/babynames/state/namesbystate.zip'
# Downloading will take awhile...
resp = requests.get(url)
# save to hard drive
f = open("/tmp/ssastates.zip", "wb")
f.write(resp.content)
f.close()

# unzip
shutil.unpack_archive("/tmp/ssastates.zip", "/tmp")
# open up coloardo

rows = open("/tmp/CO.TXT").readlines()
totes = 0
for r in rows:
    if 'Odin' in r:
        totes += int(r.split(',')[4])
print(totes)

