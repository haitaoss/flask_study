from flask import Blueprint

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
app_orders = Blueprint('app_orders', __name__)  # 指定__name__就是为了找到一个区域给他放staitc，templates


@app_orders.route('/get_orders')
def get_orders():
    return 'get orders page'


@app_orders.route('/post_orders')
def post_orders():
    return 'post orders page'
