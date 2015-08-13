# The currently serving U.S. congressmember with the most Twitter followers
from math import ceil
import csv
import json
import os
import requests
import tweepy
# You need to have a Twitter account and register as a developer:
# http://www.compjour.org/tutorials/getting-started-with-tweepy/
# Your credentials JSON file should look like this:
# {
#     "access_token": "AAAA",
#     "access_token_secret": "BBBB",
#     "consumer_secret": "CCCC",
#     "consumer_key": "DDDDD"
# }
# Twitter helper methods
DEFAULT_TWITTER_CREDS_PATH = '~/.creds/me.json' # put your own path here
def get_api(credsfile = DEFAULT_TWITTER_CREDS_PATH):
    """
    Takes care of the Twitter OAuth authentication process and
    creates an API-handler to execute commands on Twitter

    Arguments:
      - credsfile (str): the full path of the filename that contains a JSON
        file with credentials for Twitter

    Returns:
      A tweepy.api.API object

    """
    fn = os.path.expanduser(credsfile)  # get the full path in case the ~ is used
    c = json.load(open(fn))
    # Get authentication token
    auth = tweepy.OAuthHandler(consumer_key = c['consumer_key'],
                               consumer_secret = c['consumer_secret'])
    auth.set_access_token(c['access_token'], c['access_token_secret'])
    # create an API handler
    return tweepy.API(auth)

# gets a whole bunch of profile information from a batch of screen_names
BATCH_SIZE = 100
def get_profiles_from_screen_names(snames):
    api = get_api()
    profiles = []
    for i in range(ceil(len(snames) / BATCH_SIZE)):
        s = i * BATCH_SIZE
        bnames = snames[s:(s + BATCH_SIZE)]
        for user in api.lookup_users(screen_names = bnames):
            profiles.append(user._json)
    return profiles
# Step 1.
# Basically, you have to rejigger 18.py:
# (The number of U.S. congressmembers who have Twitter accounts, according to Sunlight Foundation data)
# info https://sunlightlabs.github.io/congress/#legislator-spreadsheet
csvurl = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
rows = csv.DictReader(requests.get(csvurl).text.splitlines())
# note that spreadsheet includes non-sitting legislators, thus the use
# of 'in_office' attribute to filter
legislators = [r for r in rows if r['twitter_id'] and r['in_office'] == '1']
# now call twitter
twitter_profiles = get_profiles_from_screen_names([x['twitter_id'] for x in legislators])
# match up legislators with profiles:
for lx in legislators:
    ta = [t for t in twitter_profiles if lx['twitter_id'].lower() == t['screen_name'].lower()]
    lx['twitter_profile'] = ta[0] if ta else None

def fooey(x):
    t = x['twitter_profile']
    return t['followers_count'] if t else 0

q = max(legislators, key = fooey)
print(q['title'], q['firstname'], q['middlename'], q['lastname'], q['state'])
# Sen John S. McCain AZ


