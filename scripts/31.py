# The number of proposed U.S. federal regulations in which comments are due within the next 3 days

# Note:
# This exercise is a major snafu on my part, as I assigned it thinking you
#   could easily scrape it from the front page.
#   However, the HTML of the results is generated client side, after an AJAX
#   request to whatever-the-f-ck this serialzed data format is:
#   GET http://www.regulations.gov/dispatch/LoadRegulationsClosingSoon
#   Response:
#   //OK[21,20,19,3,18,17,16,3,15,14,13,3,12,11,10,3,9,8,7,3,6,5,4,3,6,2,1,["gov.egov.erule.regs.shared.dispatch.LoadRegulationsClosingSoonResult/4107109627","java.util.ArrayList/4159755760","gov.regulations.common.models.DimensionValueModel/244318028","41","Today","8075","83","3 Days","8096","194","7 Days","8076","436","15 Days","8097","766","30 Days","8077","1133","90 Days","8078"],0,7]
#
# Reverse engineering is not a fun-type of challenge. For this particular exercise,
#  though, the answer can be found through a simple API call.
#
#
# The API dev docs are here: http://regulationsgov.github.io/developers/
#
# Specifically, the documents.json endpoint described here:
# http://regulationsgov.github.io/developers/console/#!/documents.json/documents_get_0
#
# This endpoint has 1 parameter necessary for this exercise:
#
# - cs: Comment Period Closing Soon; the value is an integer for number of days
#       until closing
import requests
BASE_URL = 'http://api.data.gov/regulations/v3/documents.json'
my_params = {'api_key': 'DEMO_KEY', 'cs': 3}
resp = requests.get(BASE_URL, params = my_params)
print(resp.json()['totalNumRecords'])
