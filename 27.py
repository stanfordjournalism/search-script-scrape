# The number of Class I Drug Recalls issued by the U.S. Food and Drug Administration since 2012
# Caveat: the FDA page says this:
#   NOTE: The recalls on the list are generally Class I.,
#   which means there is a reasonable probability that the
#   use of or exposure to a violative product will cause
#   serious adverse health consequences or death.
#
# This script assumes the recalls are all Class I, for simplicity sake
from lxml import html
import requests
url = 'http://www.fda.gov/Drugs/DrugSafety/DrugRecalls/default.htm'
doc = html.fromstring(requests.get(url).text)
links = doc.cssselect('.col-md-6.col-md-push-3.middle-column linktitle')
print(len(links))
