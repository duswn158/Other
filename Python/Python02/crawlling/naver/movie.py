#-*-coding:utf-8*-

from bs4 import BeautifulSoup
import urllib.request


resp = urllib.request.urlopen("https://movie.naver.com/movie/running/current.nhn")
#print(resp)
soup = BeautifulSoup(resp, 'html.parser')
#print(soup)

# class가 lst_dsc 인 dl 태그 전부
movies = soup.find_all('dl', class_='lst_dsc')
#print(movies)
#print(movies[0])

#제목과 별점만 출력하자.
for movie in movies:
    # find 만 하면 가장 위에있는 a태그만 가져온다
    title = movie.find('a').text
    star = movie.find('span',class_='num').text
    print('{} [{}]'.format(title,star)) 