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

db = SQLAlchemy(app)


class Role(db.Model):
    """用户角色表"""
    __tablename__ = 'tbl_roles'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship('User', backref='role')  # 这是从模型类考虑。


class User(db.Model):
    """用户表"""
    __tablename__ = 'tbl_users'  # 指明数据库的表明
    id = db.Column(db.INTEGER, primary_key=True)  # 整型的逐渐，默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))  # 这是从低层来考虑


@app.route('/')
def index():
    return 'index page'


if __name__ == '__main__':
    # 通过db的方式
    # 清除数据库里面的所有数据（数据库刚创建出来就用来爽一爽，别瞎用）
    db.drop_all()
    # 创建所有的表
    db.create_all()
    # app.run(host='0.0.0.0', port=8080, debug=True)
