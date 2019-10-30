# coding:utf-8
from flask import Flask, request
import sys

# 创建flask应用
app = Flask(__name__)


@app.route(r'/upload', methods=['POST'])
def upload():
    """接受前段传送过来的文件"""
    file_obj = request.files.get('pic')
    if file_obj is None:
        # 表示没有发送文件
        return '未上传文件'
    # 将文件保存到本地
    # with open('./demo.jpg', 'wb') as f:
    #     # 向文件写内容
    #     data = file_obj.read()
    #     f.write(data)
    # 直接使用上传的文件对象里面的save方法保存
    file_obj.save("./demo1.jpg")
    return '上传成功'


# 启动flask web服务
if __name__ == '__main__':
    # print(sys.path)
    app.run(host='192.168.205.148', port=8080, debug=True)
