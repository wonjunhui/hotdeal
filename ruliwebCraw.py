# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
import re

basic_url = "http://bbs.ruliweb.com/market/board/1020/read/25415"

fp = urllib.request.urlopen(basic_url)
source = fp.read()
fp.close()

soup = BeautifulSoup(source, 'html.parser')
title = soup.find("span", class_="subject_text")
title = title.get_text()

link = soup.find("div", class_="source_url")
link = link.find("a")
link = link.get_text()

images = []
img = soup.find("div", class_="view_content")
for imged in img.find_all("img"):
    images.append(imged.get("src"))

print(basic_url)
print(title)
print(link)
print(images)
