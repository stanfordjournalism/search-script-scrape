# Number of FDA-approved prescription drugs with GlaxoSmithKline as the applicant holder
# landing page:
# http://www.accessdata.fda.gov/scripts/cder/ob/docs/queryah.cfm
import re
import requests
formurl = 'http://www.accessdata.fda.gov/scripts/cder/ob/docs/tempah.cfm'
post_params = {'Sponsor': 'GlaxoSmithKline', 'table1': 'OB_Rx'}
resp = requests.post(formurl, data = post_params)
# Displaying records 1 to 88 of 88
m = re.search('(?<=Displaying records) *[\d,]+ *to *[\d,]+ *of *([\d,]+)', resp.text)
print(m.groups()[0])
