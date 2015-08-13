# Since 2002, the most commonly occurring winning number in New York's Lottery Mega Millions
from collections import Counter
import requests
c = Counter()
data = requests.get('https://data.ny.gov/resource/5xaw-6ayf.json').json()
for d in data:
    c.update(d['winning_numbers'].split(' '))

print(c.most_common()[0][0])
