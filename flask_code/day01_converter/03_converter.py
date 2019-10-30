# coding:utf-8

from flask import Flask,redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 这种语法叫做转换器(就是按照你指明的类型，把参数进行转换)
# 127.0.0.1:5000/goods/123
# @app.route(r'/goods/<int:goods_id>')
@app.route(r'/goods/<goods_id>')  # 不加转换器类型，默认是普通的字符串规则（除了/的字符）
# 比如这样子是访问不到的，http://192.168.205.148:8080/goods/
def goods_detail(goods_id):
    return 'goods detail page %s' % goods_id


# 1.定义自己的转换器
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[34578]\d{9}'


class RegexConverter(BaseConverter):
    """"""

    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个对象的这个属性，来进行路由的匹配
        self.regex = regex

    def to_python(self, value):
        """匹配正则正确，value就是匹配到的正则字符串
        这个方法的返回值就是试图函数的对应的参数的值
        所以我们可以在这里做坏事
        """

        print("to_python方法被调用%s" % str(value))
        return 'abc'

    def to_url(self, value):
        """使用url_for方法的时候被调用"""
        print('to_url方法被调用')
        return '18389356431'


# 2.设置将自定义的转换器添加到flask的应用中
app.url_map.converters['re'] = RegexConverter

app.url_map.converters['mobile'] = MobileConverter


# 3.使用自定义的转换器
# http://192.168.205.148:8080/send/18389356431
# 过程，通过正则匹配到这个路由地址，看到re这个转换器
# 就会去app.url_map.converter字典中找到对应的类，这里就是找到RegexConverter
# 然后会创建出这个类的实例对象，调用里面的regex属性匹配
# re(r'1[34578]\d{9}')等价于RegexConverter(app.url_map,r'1[34578]\d{9}'),第一个常数是flask帮我们传递的
# 就是说，他在构造对象的时候，会传递整个应用的url_map过去还有我们写的参数
# 最后会读取这个对象的regex属性来匹配我们的地址
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
# @app.route(r'/send/<mobile():mobile>')
# 这个就是，通过转换器的名字，找到Mobile这个类，创建出这个类的实例对象,flask会帮我们传递url_map这个参数过去
# 如果我们不想传递参数，可以写成@app.route(r'/send/<mobile:mobile>')
# 调用实例对象里面的regex属性匹配我们的访问地址
def send_sms(mobile):
    return 'send sms to %s' % mobile


@app.route(r'/index')
def index():
    # /send/
    # url = url_for('send_sms', mobile='18389356431') #这个参数符合的时候，会调用转换器的to_url方法
    url = url_for('send_sms', mobile='111111')  # 参数不符合的时候，也会执行to_url方法
    # 这就证明这里只会根据试图函数的名字,以及转换器参数的名字去调用转换器里面的to_url方法
    # 指定转换器的名字的目的，如果有多个转换器，可以通过名字的方法会来决定调用完to_url方法之后，根据什么位置
    # 拼接出访问地址
    # /send/18389356431
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map 可以查看整个flask中的路由信息
    # print(app.url_map)
    # print(app.url_map.converters)
    app.run(host='192.168.205.148', port=8080, debug=True)  # DEBUG这个参数很特殊，可以在启动应用的时候设置，
