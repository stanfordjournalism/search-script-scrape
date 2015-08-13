# Number of times Rep. Darrell Issa's remarks have made it onto the Congressional Record
from lxml import html
import requests

baseurl = "https://www.congress.gov/search"
atts = {"source":"congrecord","crHouseMemberRemarks":"Issa, Darrell E. [R-CA]"}
doc = html.fromstring(requests.get(baseurl, params = atts).text)
t = doc.cssselect(".results-number")[0].text_content()
print(t.split('of')[-1].strip().replace(',', ''))
