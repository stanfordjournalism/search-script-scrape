import requests
url = 'https://analytics.usa.gov/data/live/realtime.json'
j = requests.get(url).json()
print(j['data'][0]['active_visitors'])
