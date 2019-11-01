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
    """
      # 创建对象
    role1 = Role(name='admin')
    # session记录对象任务
    db.session.add(role1)
    # 提交任务到数据库中
    db.session.commit()

    我们创建的role1对象的id是没有值的，当执行完commit之后，数据库就多了一条记录（主键是自动增加）
    由于设置了自动跟踪，所以提交之后role1对象里面的id属性就有值了
    """

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

    # 不涉及表的修改，只要退出交互模型在进入就更新了
    users = db.relationship('User', backref='role')  # 这是从模型类考虑。

    def __repr__(self):
        """定义之后，可以让显示对象的时候更直观"""
        return "Role Object: name = %s " % self.name


class User(db.Model):
    """用户表"""
    __tablename__ = 'tbl_users'  # 指明数据库的表明
    id = db.Column(db.INTEGER, primary_key=True)  # 整型的逐渐，默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))  # 这是从低层来考虑

    def __repr__(self):
        return "User Object: name = %s " % self.name


@app.route('/')
def index():
    return 'index page'


if __name__ == '__main__':
    # 通过db的方式
    # 清除数据库里面的所有数据（数据库刚创建出来就用来爽一爽，别瞎用）
    db.drop_all()
    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name='admin')
    # session记录对象任务
    db.session.add(role1)
    # 提交任务到数据库中
    db.session.commit()

    role2 = Role(name='stuff')
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)
    # 一次保存多条数据
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
