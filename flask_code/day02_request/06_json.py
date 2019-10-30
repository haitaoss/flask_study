# coding:utf-8
from flask import Flask, jsonify
import json

# 创建应用
app = Flask(__name__)


# 返回json数据的方法
@app.route('/index')
def index():
    # json就是字符串
    data = {
        'name': 'python',
        'age': 18
    }
    # 第一种方式，首先将字典变成json字符串在响应到客户端
    # json.dumps(字典) 将python的字典转换为json字符串
    # json.loads(json字符串) 将字符串转换为字典，或者使用eval函数，可以将字符串变成对应的python的数据类型
    # json_str = json.dumps(data)
    # return json_str,'200',{'Content-Type':'application/json'}

    # 第二种方式
    # jsonify 帮助转换json数据，并设置响应头 Content-Type 为application\json
    # return jsonify(data)
    # 第三种方式，
    return jsonify(city='hainan')

    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
