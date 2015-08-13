# The total number of publications produced by the U.S. Government Accountability Office
import requests
import re
url = 'http://www.gao.gov/browse/date/custom'
txt = requests.get(url).text
# Browsing Publications by Date  (1 - 10 of 53,004 items)  in Custom Date Range
mx = re.search('Browsing Publications by Date.+', txt).group()
m = re.search('[,\d]+(?= +items)', mx).group()
print(m)
