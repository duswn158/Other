#-*-coding:utf-8*-

'''
chrome webdriver
- 84.0.4147.30 버전 다운로드
$ pip install selenium
'''

from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/explore/tags/' + input('search keyword : ')

driver = webdriver.Chrome('C:/test/chromedriver.exe')
driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

img_list = soup.find_all('div', {'class' : 'KL4Bh'})
print(img_list)

# img 태그에 src속성만 뽑아오자~ (숙제)