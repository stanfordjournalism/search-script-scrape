# In the most recently transcribed Supreme Court argument, the number of times laughter broke out
from lxml import html
from subprocess import check_output
from urllib.parse import urljoin
import requests
url = 'http://www.supremecourt.gov/oral_arguments/argument_transcript.aspx'
doc = html.fromstring(requests.get(url).text)
# get the most recent ruling, e.g. the top of table
href = doc.cssselect('table.datatables tr a')[0].attrib['href']
# download PDF
pdf_url = urljoin(url, href)
with open("/tmp/t.pdf", 'wb') as f:
    f.write(requests.get(pdf_url).content)
# punt to shell and run pdftotext
# http://www.foolabs.com/xpdf/download.html
txt = check_output("pdftotext -layout /tmp/t.pdf -", shell = True).decode()
print(txt.count("(Laughter.)"))





