#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from time import time

x = 0
for x in range(0, 6151, 75):
    link = "https://bugs.launchpad.net/ubuntu/+bugs?search=Search&field.importance=High&field.status=New&field.status=Incomplete&field.status=Confirmed&field.status=Triaged&field.status=In%20Progress&field.status=Fix%20Committed&orderby=-importance&memo=" + str(x) + "&start=" + str(x)
    print("Scraping data from: ", link)
