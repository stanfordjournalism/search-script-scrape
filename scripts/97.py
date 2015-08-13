# The New York school with the highest rate of religious exemptions to vaccinations
import requests
url = 'https://health.data.ny.gov/resource/5pme-xbs5.json'
data = requests.get(url).json()

def foo(d):
    return float(d['percentreligiousexemptions'])

school = max([r for r in data if '2014' in r['report_period']], key = foo)
print(school['schoolname'])
