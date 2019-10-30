# coding:utf-8

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route(r"/")  # 默认是GET请求方式
def index():
    """定义师徒函数"""
    return "hello flask"


# 通过methods限定访问方式
@app.route(r'/post_only', methods=['POST', 'GET'])
def post_only():
    return 'post only page'


@app.route(r'/hello', methods=['POST'])
def hello():
    return 'hello1'


@app.route(r'/hello', methods=['GET'])
def hello2():
    return 'hello2'


# 一个视图函数配置连个路由
@app.route(r'/hi1')
@app.route(r'/hi2')
def hi():
    return 'hi page'


@app.route(r'/login')
def login():
    # url = '/'
    # 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    url = url_for('index')  # 通过视图函数找到，url正则，和我们的django不一样
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map 可以查看整个flask中的路由信息
    print(app.url_map)
    app.run(host='192.168.205.148', port=8080, debug=True)  # DEBUG这个参数很特殊，可以在启动应用的时候设置，
