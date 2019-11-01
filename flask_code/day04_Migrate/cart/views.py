# 查找过程，在当前目录下没有找到，就去看看init文件中找
from . import app_cart
from flask import render_template


@app_cart.route('/get_cart')
def get_cart():
    return render_template('cart.html')
