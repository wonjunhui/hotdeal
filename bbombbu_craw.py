# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

basic_url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=2&divpage=54&&no=310581"

fp = urllib.request.urlopen(basic_url)
source = fp.read()
fp.close()

soup = BeautifulSoup(source, 'html.parser')
title = soup.find("font", class_="view_title2")
print(title.get_text())
