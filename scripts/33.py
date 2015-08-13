# The number of FDA-approved, but now discontinued drug products that contain Fentanyl as an active ingredient
# landing page:
# http://www.accessdata.fda.gov/scripts/cder/ob/docs/tempai.cfm
# search page:
# http://www.accessdata.fda.gov/scripts/cder/ob/docs/queryai.cfm
import re
import requests

formurl = 'http://www.accessdata.fda.gov/scripts/cder/ob/docs/tempai.cfm'
post_params = {'Generic_Name': 'Fentanyl', 'table1': 'OB_Disc'}
resp = requests.post(formurl, data = post_params)
# Displaying records 1 to 29 of 29
m = re.search('(?<=Displaying records) *[\d,]+ *to *[\d,]+ *of *([\d,]+)', resp.text)
print(m.groups()[0])
