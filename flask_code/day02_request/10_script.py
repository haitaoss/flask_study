# coding:utf-8
from flask import Flask
from flask_script import Manager  # 启动命令的管理类

# 创建应用
app = Flask(__name__)

# 创建Manager管理对象
manager = Manager(app)  # 让这个manager管理那个flask应用，所以需要传入Flask应用


@app.route('/index')
def index():
    return 'index page'


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)
    # 通过管理对象来启动flask
    manager.run()
