# The number of people who visited a U.S. government website using Internet Explorer 6.0 in the last 90 days
import requests
r = requests.get("https://analytics.usa.gov/data/live/ie.json")
print(r.json()['totals']['ie_version']['6.0'])
