#-*-coding:utf-8*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return '''
        <a href="/hello">hello</a><br>
        <input type='button' value='hello' onclick='location.href="/hello/name" />
    '''

# 그냥 hello로 들어오면 name = None 이고 값이 들어오면 name에 값이 들어온다
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    # hello.html을 그릴때 name변수에 name값을 전달한다 자바에 setAttribute와 비슷
    return render_template("hello.html", name=name)

@app.route('/test', methods=['POST'])
def test():
    return render_template("test.html", test=request.form['command'])

if __name__ == '__main__':
    app.run(host='localhost', port='8585')