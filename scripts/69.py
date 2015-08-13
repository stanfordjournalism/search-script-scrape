# The average number of comments on the last 50 posts on NASA's official Instagram account
from urllib.parse import urljoin
import os
import requests
DOMAIN = 'https://api.instagram.com/'
USERNAME = 'nasa'
ITEM_COUNT = 50
# note: I've specified INSTAGRAM_TOKEN in my ~/.bash_profile
atts = {'access_token': os.environ.get('INSTAGRAM_TOKEN')}
# unless you know NASA's Instagram ID by memory, you'll
# have to hit up the search endpoint to get it
# docs: http://instagram.com/developer/endpoints/users/#get_users_search
search_path = '/v1/users/search'
search_url = urljoin(DOMAIN, search_path)
searchatts = atts.copy()
searchatts['q'] = USERNAME
search_results = requests.get(search_url, params = searchatts).json()
uid = search_results['data'][0]['id']

# now we can retrieve media information
# http://instagram.com/developer/endpoints/users/#get_users_media_recent
media_path = '/v1/users/%s/media/recent' % uid
media_url = urljoin(DOMAIN, media_path)
mediaatts = atts.copy()
mediaatts['count'] = ITEM_COUNT
# for whatever reason, the count of returned items is
# always less than the requested count...so keep going
# until we reach ITEM_COUNT
items = []
while len(items) < 50:
    resp = requests.get(media_url, params = mediaatts).json()
    data = resp['data']
    if len(data) > 0:
        items.extend(data)
        mediaatts['max_id'] = data[-1]['id']
    else:
        break

ccount = sum([i['comments']['count'] for i in items[0:ITEM_COUNT]])
print(ccount // len(items))
