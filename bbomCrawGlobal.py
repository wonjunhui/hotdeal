# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
import re

basic_url = "http://www.ppomppu.co.kr/zboard/view.php?id=ppomppu4&page=1&divpage=19&no=103698"

fp = urllib.request.urlopen(basic_url)
source = fp.read()
fp.close()

soup = BeautifulSoup(source, 'html.parser')
title = soup.find("font", class_="view_title2")
title = title.get_text()

link = soup.find("div", class_="wordfix")
link = link.get_text()
link = re.sub('링크: ', '',link)

images = []
img = soup.find_all("table", class_="pic_bg")
img = img[2]
for imged in img.find_all("img"):
    images.append("http:"+imged.get("src"))

print(basic_url)
print(title)
print(link)
print(images)
