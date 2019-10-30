# coding:utf-8
from flask import Flask, session, g

# 创建应用
app = Flask(__name__)

# flask的session需要用到的秘钥字符串，没有就无法设置session
app.config['SECRET_KEY'] = 'SDJFASDFSFKLSDFJL'


# flask默认把session数据保存到cookie中
@app.route('/login')
def login():
    # 设置session数据
    session['name'] = 'python'
    session['mobile'] = '110'

    return 'login'


def say_hello():
    pass


@app.route('/index')
def index():
    # 获取session数据
    name = session.get('name')
    return 'hello %s ' % name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
