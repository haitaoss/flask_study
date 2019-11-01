# 初始化文件，如果要导入一个python的包，就会先执行包下面的这个文件
# 在这里就写初始化的数据
from flask import Blueprint

# print(__name__)
# 创建了一个蓝图
app_cart = Blueprint('app_cart',
                     __name__,
                     static_folder='static',
                     static_url_path='static',
                     template_folder='templates')  # 小名字，寻找目录的名字

# 在__init__文件被执行的时候，把试图加载进来，让蓝图与应用程序知道有试图的存在
from .views import get_cart
