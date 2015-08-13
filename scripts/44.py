# Number of people visiting a U.S. government website right now
# via: https://analytics.usa.gov/
import requests
url = 'https://analytics.usa.gov/data/live/realtime.json'
j = requests.get(url).json()
print(j['data'][0]['active_visitors'])
