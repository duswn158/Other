# -*- coding:utf-8 -*-



from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests
import json
import flask_cors



app= Flask(__name__)
flask_cors.CORS(app)


@app.route('/')
def root():
    return render_template('index.html')
    
    
@app.route('/crawling')
def crawling():
    resp = requests.get('https://movie.naver.com/movie/running/current.nhn')
    soup=BeautifulSoup(resp.text,'html.parser')
    
    
    #naver영화에서 제목과 별점을 크롤링하여 json으로 리턴하자 
    #   {"movies" : [{"title":"다만악에서 구하소서","star":"7.79",....}] }
    movies = soup.find_all('dl',{'class':'lst_dsc'})
    #print(movies)
    
    
    res_list = list()
    
    for movie in movies:
        res = dict()
        res['title']= movie.find('a').text
        res['star']= movie.select('.num')[0].text
        res_list.append(res)
        #[{"title":"다만악에서 구하소서","star":"7.79",....}]
        
    res_dict={}
    res_dict['movies']=res_list
    
    
    res_json=json.dumps(res_dict, ensure_ascii=False)
    print(res_json)
    
    return res_json
    
        
        
        


if __name__== '__main__':
    app.run(port='8585')








