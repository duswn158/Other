#-*-coding:utf-8*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_root():
    return '<h1><a href="/test/admin">parameter test</a></h1>'

@app.route('/test/<id>')
def hello_test(id):
    return'<h1>hello, ' + id + '</h1> <a href="/">go root</a>'

if __name__ == '__main__':
    app.run()