# Number of Titles that have changed in the United States Code since its last release point
# Note: the div class of "usctitlechanged" is used to mark such titles
import requests
url = 'http://uscode.house.gov/download/download.shtml'
txt = requests.get(url).text
print(txt.count('class="usctitlechanged" id'))
