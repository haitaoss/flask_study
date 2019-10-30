# coding:utf-8
from flask import Flask, make_response, request

# 创建应用
app = Flask(__name__)


# 返回json数据的方法
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('success')
    # 设置cookie，默认有效期是临时cookie，浏览器关闭就失效
    # resp.set_cookie('itcast1', 'python1')
    # max_age 设置有效期，单位是秒
    # resp.set_cookie('itcast2', 'python2', max_age=3600)
    # 本质是设置响应头，所以我们可以设置响应头
    resp.headers['Set-Cookie']='itcast1=111iyiyi; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=36000; Path=/'

    return resp


@app.route('/get_cookie')
def get_cookie():
    c = request.cookies.get('itcast1')
    return c


@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('del success')
    # 删除cookie，本质是设置cookie的有效期，因为我们不能命令浏览器删除cookie只能设置过期时间
    resp.delete_cookie('itcast1')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
