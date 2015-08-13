# Number of FOIA requests made to the Chicago Public Library
import csv
import requests
url = 'https://data.cityofchicago.org/api/views/n379-5uzu/rows.csv?accessType=DOWNLOAD'
data = list(csv.DictReader(requests.get(url).text.splitlines()))
print(len(data))
