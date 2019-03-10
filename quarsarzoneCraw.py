# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
import re

basic_url = "https://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo"
basic_link = "https://www.clien.net/"

fp = urllib.request.urlopen(basic_url)
source = fp.read()
fp.close()
soup = BeautifulSoup(source, 'html.parser')

link = soup.findAll("a", class_="item-subject")
print(link)
# link = link.attrs['href']
# link = basic_link+link
#
# fp = urllib.request.urlopen(link)
# source = fp.read()
# fp.close()
# soup = BeautifulSoup(source, 'html.parser')
#
# title = soup.find("h3", class_="post_subject")
# title = title.findAll("span")
# title = title[1].get_text()
#
# product_link = soup.find("a", class_="url")
# product_link = product_link.attrs['href']
#
# images = []
# img = soup.find("div", class_="post_article fr-view")
# for imged in img.find_all("img"):
#     images.append(imged.get("src"))
#
# print(link)
# print(title)
# print(product_link)
# print(images)
