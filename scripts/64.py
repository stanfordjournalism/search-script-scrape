# From March 1 to 7, 2015, the number of times in which designated FDA policy makers met with persons outside the U.S. federal executive branch
# this is a hardcoded URL
url = 'http://www.fda.gov/NewsEvents/MeetingsConferencesWorkshops/PastMeetingsWithFDAOfficials/ucm439318.htm'
import requests
print(requests.get(url).text.count('Event Date'))
