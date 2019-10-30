# coding:utf-8
from flask import Flask, request

# 创建flask应用
app = Flask(__name__)


# 借口 api
# 127.0.0.1:5000/index?city=shenzhen 问号后面的叫查询字符串，QueryString
@app.route(r'/index', methods=['POST', 'GET'])
def index():
    # 从request中包含了前段发送古来的所有请求信息
    # 通过request.form可以直接提取请求体中的表单格式的数据，是一个类字典的对象
    # 通过get方法只能拿到多个同名参数的第一个的值
    name = request.form.get("name")
    age = request.form.get("age")
    name_list = request.form.getlist('name')
    # args是用来提取url中的参数（查询字符串）
    city = request.args.get('city')
    print("request.data:%s" % request.data)  # raw和binary格式的数据如json字符串
    return 'hello name=%s, age=%s, citry=%s,name_list=%s' % (name, age, city, name_list)


# 启动flask web服务
if __name__ == '__main__':
    app.run(host='192.168.205.148', port=8080, debug=True)
