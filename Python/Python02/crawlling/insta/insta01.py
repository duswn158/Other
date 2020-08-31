#-*-coding:utf-8*-

from bs4 import BeautifulSoup
import requests

tag = input('search keyword : ')
url = 'https://www.instagram.com/explore/tags/' + tag
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

# print(soup)

# None이 나온다 웹페이지가 모두 로딩되기 전에 돌기 때문
# 즉 랜더링이 되지 않은상태에서 가져옴
res = soup.find('div', {'class' : 'KL4Bh'})
print(res)