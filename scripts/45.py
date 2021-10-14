# The number of security alerts issued by US-CERT in the current year

import requests
from lxml import html
from bs4 import BeautifulSoup

def getTotalSecurityCount(year):

    counter = 0
    result = 0
    flag = True

    try:

        while flag:

            url = "https://www.us-cert.gov/ncas/alerts/" + year + "?page=" + str(counter)
            page = requests.get(url)

            if page.status_code == 200:

                bs = BeautifulSoup(page.text, "html.parser")

                r = bs.find_all("div", {"class": "views-field views-field-title"})
                
                if len(r) > 0:
                    result = result + len(r)
                    counter = counter + 1
                else:
                    flag = False

            else:
                flag = False
    except:
        print("Exception raised")
    

    return result

year = input("Input current year: ")

print(f"Total security alert in {year} is: {getTotalSecurityCount(year)}")
