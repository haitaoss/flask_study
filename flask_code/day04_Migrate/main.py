from flask import Flask
from goods import get_goods
from users import register
from orders import app_orders
from cart import app_cart

app = Flask(__name__)

# 使用装饰器解决模块导入问题
# @app.route('/get_goods')
# app.route('/get_goods')(get_goods)
# app.route('/register')(register)
xx = app.route('/get_goods')
xx(get_goods)
xx2 = app.route('/register')
xx2(register)

# 注册蓝图
app.register_blueprint(app_orders, url_prefix='/orders')
app.register_blueprint(app_cart, url_prefix='/cart')


@app.route('/')
def index():
    print(app.url_map)
    return 'index page'


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='192.168.205.148', port=8080, debug=True)
