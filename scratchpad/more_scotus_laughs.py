# Modification of scripts/50.py to count all the laughs in the most recent term
from lxml import html
from subprocess import check_output
from urllib.parse import urljoin
import requests
url = 'http://www.supremecourt.gov/oral_arguments/argument_transcript.aspx'
doc = html.fromstring(requests.get(url).text)
# get all the rulings
for link in doc.cssselect('table.datatables tr a'):
    href = link.attrib['href']
    # let's store the title of the case from table cell
    casetitle = link.getnext().text_content()
    # download PDF
    pdf_url = urljoin(url, href)
    with open("/tmp/t.pdf", 'wb') as f:
        f.write(requests.get(pdf_url).content)
    # punt to shell and run pdftotext
    # http://www.foolabs.com/xpdf/download.html
    txt = check_output("pdftotext -layout /tmp/t.pdf -", shell = True).decode()
    print("%s laughs in: %s" % (txt.count("(Laughter.)"), casetitle))





