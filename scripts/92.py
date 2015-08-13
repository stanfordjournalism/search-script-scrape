# In 2012-Q4, the total amount paid by Rep. Aaron Schock to Lobair LLC, according to Congressional spending records, as compiled by the Sunlight Foundation
# real-life reference: http://www.usatoday.com/story/news/politics/2015/02/19/schock-flights-charter-house-rules/23663247/
import csv
import requests
DATA_URL = 'http://assets.sunlightfoundation.com.s3.amazonaws.com/expenditures/house/2012Q4-detail.csv'
SCHOCK_ID = 'S001179' # http://bioguide.congress.gov/scripts/biodisplay.pl?index=s001179
print("Downloading", DATA_URL)
resp = requests.get(DATA_URL)
totalamt = 0
for row in csv.DictReader(resp.text.splitlines()):
    if row['BIOGUIDE_ID'] == SCHOCK_ID and 'LOBAIR LLC' in row['PAYEE'].upper():
        totalamt += float(row['AMOUNT'])
print(totalamt)
# 880.0
