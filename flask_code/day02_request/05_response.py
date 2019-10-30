# coding:utf-8
from flask import Flask, Response, request, make_response

# 创建应用
app = Flask(__name__)


# 设置响应信息的方法
@app.route('/index')
def index():
    # 1.使用元祖，返回自定义的响应信息.python在处理多个返回值的时候，会把多个值当成一个元祖，就是会帮你在左右两边添加()
    #       响应体       状态码 响应头
    # return 'index page', 400, [('ITCAST', 'python'), ('City', 'hainan')]
    # return 'index page', 400, {'ITCAST': 'python', 'City': 'hainan'}
    # return 'index page', 666, {'ITCAST': 'python', 'City': 'hainan'} # 传递的是非标准的状态码，还可以自定义状态码的含义
    # return 'index page', '666 itcast status', {'ITCAST': 'python', 'City': 'hainan'}
    # return 'index page', '666 itcast status'  # 顺序必须是，响应体，状态码，响应头，可以从后面开始省略，不能响应体 响应头，这是错误的

    # 2.使用make_response 来构造响应信息
    resp = make_response('index page 2')  # 参数是响应体信息
    # 得到了response对象之后，就可以通过设置这个对象的属性，来实现响应体和响应头的设置
    resp.status = '9999 itcast'  # 设置状态码，已经状态码提示信息。
    resp.headers['city'] = 'hainan'  # 设置响应头
    return resp
    pass


def test():
    # return 'xxxx', 'bbbb'
    return 'xxx'


if __name__ == '__main__':
    # print(type(test())) # 测试返回值的类型
    app.run(host='0.0.0.0', port=8080, debug=True)
