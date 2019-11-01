# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 配置数据库的连接信
class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/db_python04'

    # sqlalchmy自动跟踪数据库的修改操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 设置显示操作模型类时对应的sql语句
    SQLALCHEMY_ECHO = True


# 加载我们的配置信息
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
# 构建db的时候，他会自动从app里面找到sqlalchemy的配置信息
# 最后我们使用db就可以操作数据库了
db = SQLAlchemy(app)


# 表明的常见规范
# db_python04  -> dp_user 数据库名缩写_表明
# tbl_user -> tbl_表明
# 创建数据库模型类
class Role(db.Model):
    """用户角色表"""
    __tablename__ = 'tbl_roles'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # 为了查询方便设置的字段，在数据库表中没有这个字段
    # users关联的是User这个模型类，就是说role.users获取的是User的实例对象
    # backref就是反推，当我们使用User这个模型类的实例对象user.role获取的就是Role实例对象的模型类
    # 其实你也可以在，User模型类里面加上这个关系数据，来实现，
    # backref就相当于给User这个模型类添加了一个属性role，去啥名字都可以
    users = db.relationship('User', backref='role')  # 这是从模型类考虑。


class User(db.Model):
    """用户表"""
    __tablename__ = 'tbl_users'  # 指明数据库的表明
    id = db.Column(db.INTEGER, primary_key=True)  # 整型的逐渐，默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))  # 这是从低层来考虑


# select * from user where role_id = 1
@app.route('/')
def index():
    return 'index page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
