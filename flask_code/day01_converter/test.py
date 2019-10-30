# coding:utf-8
from flask import Flask

# 创建实例对象
app = Flask(__name__)


# 试图函数
@app.route('/test/<string:xx><int:dd>')
# http://127.0.0.1:8180/test/119922220000
# 说明匹配规则是贪婪匹配，
def test(xx, dd):
    return "xx:" + str(xx) + 'dd:' + str(dd)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(host='127.0.0.1', port=8180, debug=True)
