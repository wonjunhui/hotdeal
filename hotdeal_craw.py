from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen


from lxml import etree

# options = webdriver.ChromeOptions()
# options.add_argument('window-size=1920x1080')
#
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# options.add_argument("lang=ko_KR") # 한국어!
#
# chromedriver_path = './driver/chromedriver'
# driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
#
# index = '9274'
# driver.get('https://aagag.com/deal/?idx='+index)
# driver.implicitly_wait(3)

# driver.quit()

index = '9274'
url = 'https://aagag.com/deal/?idx='+index
html = urlopen(url).read()

htmlparser = etree.HTMLParser()
tree = etree.parse(html, htmlparser)
print(tree.xpath('//*[@id="c_main"]/h1'))

# soup = bs(html, "html.parser")


# title = soup.find("h1",class_="title")
# print(title.get_text())
#
# images = soup.find("div",id="deal_image")
# print(images)
# print(images.find('img'))