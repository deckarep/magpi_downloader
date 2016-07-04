#!/usr/bin/python
import requests
from BeautifulSoup import BeautifulSoup

def getChildren():
    r = requests.get("https://www.raspberrypi.org/magpi/issues/")
    results = []
    if r.status_code == 200:
        soup = BeautifulSoup(r.text)
        # This ugly query gets the modal popup links directly to the .pdf files themselves
        for anchor in soup.findAll('div', {"style":"text-align: center;margin-top: 5px;"}):
                results.append(anchor.a["href"])
    return results

for l in getChildren():
    print l
