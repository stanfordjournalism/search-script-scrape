# The total number of babies named Odin born in Colorado according to the Social Security Administration
import shutil
import requests
url = 'http://www.ssa.gov/OACT/babynames/state/namesbystate.zip'
# Downloading will take awhile...
print("Downloading", url)
resp = requests.get(url)
# save to hard drive
with open("/tmp/ssastates.zip", "wb") as f:
    f.write(resp.content)
# unzip
shutil.unpack_archive("/tmp/ssastates.zip", "/tmp")
# open up the file
rows = open("/tmp/CO.TXT").readlines()
totes = 0
for r in rows:
    if 'Odin' in r:
        totes += int(r.split(',')[4])
print(totes)

