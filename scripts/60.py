# Number of chapters in Title 20 (Education) of the United States Code
import requests
import re
from lxml import html
# this URL downloads the WHOLE code for education
url = 'http://uscode.house.gov/view.xhtml?path=/prelim@title20&edition=prelim'
print("Downloading", url)
txt = requests.get(url).text
doc = html.fromstring(''.join(txt.splitlines()[1:])) # skipping xml declaration
# interpretation of number of chapters can vary...I'm going to go with
# "highest number"
titles = [t.text_content().strip() for t in doc.cssselect('h3.chapter-head strong')]
m = re.search("(?<=CHAPTER )\d+", titles[-1]).group()
print(m)

