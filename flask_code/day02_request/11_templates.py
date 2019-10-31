# coding:utf-8

from flask import Flask, render_template
from flask_script import Manager

# 创建flask应用
app = Flask(__name__)


# 创建Manager对象管理Flask应用
# manager = Manager(app)


# 视图函数
@app.route('/index')
def index():
    context = {'name': u'海涛',
               'age': 18,
               'my_dict': {'city': 'hn'},
               'my_list': range(10),
               'my_int': 0
               }
    return render_template('index.html', **context)


def list_step_2(li):  # {{ list | }}
    """自定义过滤器"""
    # 从头到尾，步长为2的方式获取字符串
    return li[::2]


# 注册过滤器,第一个过滤器的函数名，第二个就是别名
app.add_template_filter(list_step_2, 'li2')


# 一步到位的写法
@app.template_filter('li3')
def list_step_3(li):  # {{ list | }}
    """自定义过滤器"""
    # 从头到尾，步长为2的方式获取字符串
    return li[::3]


# 启动flas应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # manager.run()
