# Number of Dallas officer-involved fatal shooting incidents in 2014
import requests
url = 'https://www.dallasopendata.com/resource/4gmt-jyx2.json'
data = requests.get(url).json()
records = [r for r in data if ('2014' in r['date']
                    and 'Deceased' in r['suspect_deceased_injured_or_shoot_and_miss'])]
print(len(records))
