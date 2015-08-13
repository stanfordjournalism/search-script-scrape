import requests
import re
url = "https://clinicaltrials.gov/ct2/results?recr=Open&cond=%22Alcohol-Related+Disorders%22"
r = re.search('(?<=<strong>)\d+(?= +studies found for)', requests.get(url).text)
print(r.group())
