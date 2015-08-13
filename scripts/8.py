# The number of times when a New York heart surgeon's rate of patient deaths for all cardiac surgical procedures was "significantly higher" than the statewide rate, according to New York state's analysis.
import requests
url = 'https://health.data.ny.gov/resource/dk4z-k3xb.json'
xstr = 'Rate significantly higher than Statewide Rate'
data = requests.get(url).json()
records = [r for r in data if xstr in r['comparison_results']]
print(len(records))
