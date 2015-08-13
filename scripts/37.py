# The last time the CIA's Leadership page has been updated
import requests
import re
url = "https://www.cia.gov/about-cia/leadership"
txt = re.search('Last Updated:.+?(?=<br>)', requests.get(url).text).group()
print(txt)
