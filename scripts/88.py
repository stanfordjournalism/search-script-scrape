# The number of posts on TSA's Instagram account
from urllib.parse import urljoin
import os
import requests
DOMAIN = 'https://api.instagram.com/'
USERNAME = 'tsa'
# note: I've specified INSTAGRAM_TOKEN in my ~/.bash_profile
atts = {'access_token': os.environ.get('INSTAGRAM_TOKEN')}
# unless you know TSA's Instagram ID by memory, you'll
# have to hit up the search endpoint to get it
# docs: http://instagram.com/developer/endpoints/users/#get_users_search
search_path = '/v1/users/search'
searchatts = atts.copy()
searchatts['q'] = USERNAME
search_results = requests.get(urljoin(DOMAIN, search_path), params = searchatts).json()
uid = search_results['data'][0]['id']

# now we can retrieve profile information
# https://instagram.com/developer/endpoints/users/#get_users
user_path = '/v1/users/%s/' % uid
profile = requests.get(urljoin(DOMAIN, user_path), params = atts).json()
print(profile['data']['counts']['media'])


