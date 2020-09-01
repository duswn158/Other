#-*-coding:utf-8*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_root():
    return '<h1><a href="/flask">gello, flask</a></h1>'

@app.route('/flask')
def hello_flask():
    return '<h1><a href="/">go root</a></h1>'

if __name__ == '__main__':
    app.run()
    
