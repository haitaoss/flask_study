# coding:utf-8
# python2需要指定编码，才能支持中文

from flask import Flask, current_app
import demo

# 创建flask的应用对象
# __name__是一个魔法变量，指的是当前模块的名字
# 这里的意思是以__name__这个模块文件的所在，目录作为项目的根目录
# 默认这个目录中的static为静态目录，templates为模板目录

# app = Flask('sfasdfdjs')  # 如果模块不存在，就会认为当前模块名字就是
# app = Flask("__main__")  # 运行当前文件，所以__name__就是__main__，即这个写法在这里不会出错
# app = Flask(__name__)
app = Flask(__name__,
            static_url_path='/python',  # static_url_path='/python',映射路径
            # 主要目的是，区分浏览器访问的是不是静态资源，而不是一个试图

            # 就是用户访问 /python/1.html，框架（django，flask）一匹配到static（就是我们设置的static_url_path）
            # 框架就认为我们访问的是静态资源
            # 就不在去找试图函数，而是直接去配置好的静态文件目录找资源
            static_folder='static',  # 静态文件的目录，默认就是当前项目目录下面的static
            template_folder='templates')  # 模板文件目录，默认就是当前项目下面的templates


# 配置参数的使用方式
# 1.使用配置文件
# app.config.from_pyfile('config.cfg')  # 不谢路径就是当前项目路径


# 2.使用对象配置参数,开发使用这种方式
class Config(object):
    DEBUG = True
    ITCAST = 'python'


app.config.from_object(Config)  # 从类里面读取配置参数


# 3.直接操作config的字典对象
# app.config['DEBUG'] = True


@app.route(r"/")
def index():
    """定义师徒函数"""
    # a = 1 / 0

    # 读取配置参数

    # 1.直接从全局对象app的config字典中取值
    print(app.config.get('ITCAST'))

    # 2.通过current_app获取参数【导入current_app，你可以理解成是app的同名词】
    print current_app.config.get('ITCAST')
    return "hello flask"


if __name__ == '__main__':
    # 启动flask应用
    # app.run()
    # app.run(host='0.0.0.0', port=8080) # 0.0.0.0表示当前主机的IP地址都可以访问
    # app.run(host='192.168.205.148', port=8080)  # http://127.0.0.1:8080/是访问不到的
    app.run(host='192.168.205.148', port=8080, debug=True)  # DEBUG这个参数很特殊，可以在启动应用的时候设置，
