# The number of university-related datasets currently listed at data.gov
import requests
import re
url = 'http://catalog.data.gov/dataset?'
atts = {'organization_type': 'University', 'sort': 'metadata_created desc'}
txt = requests.get(url, params = atts).text
print(re.search("[0-9,]+(?= *datasets found)", txt).group().replace(',', ''))
