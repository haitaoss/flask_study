from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)


# 配置参数的类
class Config(object):
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_author_book'

    # sqlalchmy自动跟踪数据库的修改操作
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置显示操作模型类时对应的sql语句
    # SQLALCHEMY_ECHO = True
    SECRET_KEY = 'ASFSD2L424UJSAFHA'


# 加载配置

app.config.from_object(Config)
# 创建数据源
db = SQLAlchemy(app)


# 创建表单模型类
class AuthorBookForm(FlaskForm):
    """作者书籍表单模型类"""

    author_name = StringField(label='作者', validators=[DataRequired('作者必填')])
    book_name = StringField(label='书籍', validators=[DataRequired('书籍必填')])
    submit = SubmitField(label='保存')


# 创建模型类
class Author(db.Model):
    """作者模型类"""
    __tablename__ = 'tbl_authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # 方便我们查询，反向查询，反向引用
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    """书籍"""
    __tablename__ = 'tbl_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(28), unique=True)
    # 关联关系
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_authors.id'))


# 配置试图函数
@app.route('/index', methods=['POST', 'GET'])
def index():
    """"""
    # 创建表单模型类
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功

        # 获取表单数据
        author_name = form.author_name.data
        book_name = form.author_name.data
        # print(author_name, book_name)

        # 业务处理
        try:
            author = Author(name=author_name)
            db.session.add(author)
            db.session.commit()

            # book = Book(name=book_name, author_id=author.id)
            book = Book(name=book_name, author=author)  # 都可以，这里不是反射添加了属性了吗
            db.session.add(book)
            db.session.commit()
        except:
            # print(type(e))
            # 添加异常信息
            flash("图书或者作者已经存在")

        # 返回应答
    # 查询数据库
    author_li = Author.query.all()

    return render_template('author_book.html', authors=author_li, form=form)


# ajax post /delete_book
# {"book_id":x}
# @app.route('/delete_book', methods=['POST'])
# def delete_book():
#     """删除数据"""
#     # 获取数据,如果前段发送的请求体是json格式，get_json会解析成字典
#     # get_json 要求前段传送的数据的Content-Type:application/json
#     req_dict = request.get_json()
#     # book_id = request.form.get('book_id')
#     book_id = req_dict.get('book_id')
#     print("book_id:" + book_id)
#
#     # 删除数据
#     book = Book.query.get(book_id)
#     db.session.delete(book)
#     db.session.commit()
#
#     # 响应
#     return jsonify(code=0, message="OK")

@app.route('/delete_book', methods=['GET'])
def delete_book():
    """删除数据"""
    # 获取数据

    book_id = request.args.get('book_id')
    print("book_id:" + book_id)

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    # 响应
    return redirect(url_for('index'))


# 启动项目
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # db.drop_all()
    # db.create_all()
    #
    # # 生成数据
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # # 添加到session
    # db.session.add_all([au_xi, au_qian, au_san])
    # # 提交
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒', author_id=au_xi.id)
    # bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    # # 添加到session
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    #
    # # 提交
    # db.session.commit()
    # app.run(debug=True)
