# In the most recent FDA Adverse Events Reports quarterly extract, the number of patient reactions mentioning "Death"
# Note: I changed the original exercise to something a little more specific and challenging
#
# We *could* use the API:
# https://open.fda.gov/api/reference/#query-syntax
# After reading those docs, do you have no idea how to make even a simple call
#  for events and filter by date? Neither do I, so let's just go with
#  good ol' bulk data downloads:
#  http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm
import requests
from io import BytesIO
from zipfile import ZipFile
from lxml import html
from urllib.parse import urljoin
from collections import Counter
LANDING_PAGE_URL = "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm"
doc = html.fromstring(requests.get(LANDING_PAGE_URL).text)
# find the most recent FAERS ASCII zip file with good ol xpath:
links = doc.xpath("//a[linktitle[contains(text(), 'ASCII')] and contains(@href, 'zip')]")
# Presumably, they're listed in reverse chronological order:
link = links[0]
zipurl = urljoin(LANDING_PAGE_URL, link.attrib['href'])
print("Downloading", link.text_content(), ":")
print(zipurl)
resp = requests.get(zipurl) # this is going to take awhile...
with ZipFile(BytesIO(resp.content)) as zfile:
    # the zip contains many files...we want the one labeled REACYYQX.txt
    # e.g. ascii/REAC15Q1.txt
    fname = next(x.filename for x in zfile.filelist if
                                    "REAC" in x.filename and "txt" in x.filename.lower())
    print("Unzipping:", fname)
    data = zfile.read(fname).decode('latin-1').splitlines()
    # The data looks like this:
    # primaryid$caseid$pt$drug_rec_act
    # 100036412$10003641$Medication residue present$
    # 100038593$10003859$Blood count abnormal$
    # 100038593$10003859$Platelet count decreased$
    # 100038603$10003860$Abdominal pain$

    # Rather than programatically locating the "reaction" column,
    # e.g. "pt", I'm just going to hardcode it as the
    # 3rd (2nd via 0-index) column delimited by a `$` sign
    reactions = [row.split('$')[2].lower() for row in data]
    deaths = [r for r in reactions if 'death' in r]
    print("Out of %s reactions, %s mention 'death'" % (len(reactions), len(deaths)))
    # sample output for 2015Q1
    # Out of 873190 reactions, 14188 mention 'death'
