# coding:utf-8
from flask import Flask, request, url_for

# 创建应用
app = Flask(__name__)


@app.route('/index')
def index():
    print('index 被执行')
    a = 1 / 0
    return 'index page'


@app.route('/hello')
def hello():
    return 'hello'


@app.before_first_request
def handle_before_first_request():
    """在第一次请求处理之前被执行"""
    print('handle_before_first_request 被执行')


@app.before_request
def handle_before_request():
    """每次请求之前都被执行"""
    print('handle_before_request 被执行')


@app.after_request
def handle_after_request(response):
    """在每次请求之后(试图函数处理),试图函数不出现异常，被执行"""
    print('handle_after_request 被执行')
    return response


@app.teardown_request
def handle_teardown_request(response):
    """在每次请求之后都被执行(试图函数处理)，无论试图函数是否出现异常，都被执行
        工作在非调试模式时，即debug=false
    """
    path = request.path
    if path == url_for('index'):
        print('在请求钩子中判断请求的视图逻辑： index')
    elif path == url_for('hello'):
        print('在请求钩子中判断请求的视图逻辑： hello')
    print('handle_teardown_request 被执行')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
