# Number of public Github repositories maintained by the GSA's 18F organization, as listed on Github.com
import requests
url = 'https://api.github.com/orgs/18F'
data = requests.get(url).json()
print(data['public_repos'])
