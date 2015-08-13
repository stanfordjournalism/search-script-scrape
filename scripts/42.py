# The name of the Supreme Court justice who delivered the opinion in the most recently announced decision
# depends on PyPDF2 https://pythonhosted.org/PyPDF2/PdfFileReader.html
from io import BytesIO
from lxml import html
from PyPDF2 import PdfFileReader
from urllib.parse import urljoin
import requests
import re
# get the most recent ruling
url = "http://www.supremecourt.gov/opinions/slipopinions.aspx"
doc = html.fromstring(requests.get(url).text)
a = doc.cssselect('#mainbody table')[0].cssselect('tr a')[0]
# download PDF
pdf_url = urljoin(url, a.attrib['href'])
pdfbytes = BytesIO(requests.get(pdf_url).content)
pdf = PdfFileReader(pdfbytes)
# compile text of all the pages
txt = ""
for i in range(pdf.getNumPages()):
    txt += pdf.getPage(i).extractText() + "\n"
# regex match...hopefully this is *always* the text...
m = re.search("[A-Z]+, *(?:J\.|C\. J\.|JJ\.)(?=, delivered the opinion of the Court)", txt)
print(m.group())

# Sample relevant text:
# KENNEDY, J., delivered the opinion of the Court, in which GINSBURG,
# BREYER, SOTOMAYOR, and KAGAN, JJ., joined. BREYER, J., filed a concurring
# opinion. THOMAS, J., filed an opinion concurring in the judgment
# in part and dissenting in part. ROBERTS, C. J., filed a dissenting opinion,
# in which ALITO, J., joined. SCALIA, J., filed a dissenting opinion, in
# which ROBERTS, C. J., and ALITO, J., joined.
