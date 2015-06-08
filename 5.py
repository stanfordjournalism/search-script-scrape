# The name of the company cited in the most recent consumer complaint involving student loans
# note that this is a pre-made filter from:
# https://data.consumerfinance.gov/dataset/Consumer-Complaints/x94z-ydhh
import requests
from operator import itemgetter
url = "https://data.consumerfinance.gov/api/views/c8k9-ryca/rows.json?accessType=DOWNLOAD"

# If you go the JSON route with Socrata, you have to
# do an extra step of parsing metadata to get the
# desired columns...or you could just hardcode their
# positions for now
data = requests.get(url).json()
# use meta data to extract which column Company exists in
cols = data['meta']['view']['columns']
# fancier way of doing a for-loop and counter
# http://stackoverflow.com/questions/2748235/in-python-how-can-i-find-the-index-of-the-first-item-in-a-list-that-is-not-some

# get position of Date received column
d_pos = next((i for i, c in enumerate(cols) if c['name'] == 'Date received'), -1)

# get position of Company column
c_pos = next((i for i, c in enumerate(cols) if c['name'] == 'Company'), -1)

# It appears that Socrata returns the data in order of
# Date received but just in case, here's a sort
row = max(data['data'], key = itemgetter(d_pos))
print(row[c_pos])
