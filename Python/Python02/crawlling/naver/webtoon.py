#-*-coding:utf-8*-

# $ pip install requests

from bs4 import BeautifulSoup
import requests
import json
from idlelib.iomenu import encoding

resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=mon')
soup = BeautifulSoup(resp.text, 'html.parser')

#print(soup)

webtoons = soup.find('ul',{'class':'img_list'})
#print(webtoon)
dl = webtoons.select('dl')

lst = list()
for chd in dl:
        title = chd.find('a').text
        star = chd.find('strong').text
        #print('{} [{}]'.format(title, star))
        tmp = {}
        tmp['title'] = title
        tmp['star'] = star
        lst.append(tmp)
# 현재는 json이 아닌 그냥 딕셔너리 안의 list [{},{}]형태이기 때문에 아래에서 한번 더 바꾸어준다
#print(lst)

# {k : [{},{},{}]} key : value(배열) 형태는 json이 가능 하기 때문에 그렇게 바꾸어주었다
res = {}
res['webtoons'] = lst
#print(res)

# json으로 바꾸어 준다 즉 k : v, k : v 형태
res_json = json.dumps(res, ensure_ascii=False)
print(res_json)

# json으로 만든걸 파일로 저장
with open('webtoons.json','w', encoding='utf-8') as f:
    f.write(res_json)