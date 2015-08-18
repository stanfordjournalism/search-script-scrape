# Number of airports with existing construction related activity
import requests
import re
resp = requests.get('https://nfdc.faa.gov/xwiki/bin/view/NFDC/Construction+Notices')
# obviously not something you do in an actual scraping solution but it gets the answer!
print(len(re.findall("Construction\+Notices/.+?\.pdf", resp.text)))
