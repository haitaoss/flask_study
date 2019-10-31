# coding:utf-8
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    if name == 'zhangsan' and pwd == 'admin':
        return 'login success'
    # 使用abort函数可以立即终止试图函数的执行
    # 并可以返回给前端特定的信息
    # 1.传递状态码信息,最常用就是返回状态码
    abort(404)
    # 2.传递相应体信息，还不如直接return ‘login failed’
    # abort(Response('login failed'))


@app.errorhandler(404)
def handle_404_error(err):
    """自定义的处理404错误的试图方法"""
    # 这个函数的返回值，会是前段用户看到的最终结果
    return '出现了404错误，错误信息：%s' % err


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
