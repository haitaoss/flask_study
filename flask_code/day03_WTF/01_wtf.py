# coding:utf-8
from flask import Flask, session, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo


""""
流程
    我们使用flask_wtf扩展包，导入FlaskForm这个类，有助于表单的校验
    
当我们使用get请求访问的时候，form = Register()这句代码不会执行类里面的validators
当我们是有post访问的时候，form = Register()会执行里面的validators
"""
app = Flask(__name__)

app.config["SECRET_KEY"] = "SFASDFSFSAWERUIOWE7934887"


# 定义表单的模型类
class Register(FlaskForm):
    """自定义的注册表单模型类"""
    #                       说明标签        验证器
    # DataRequired 保证数据必须填写，并且不能为空
    user_name = StringField(label=u'用户名', validators=[DataRequired(u"用户名不能为空")])
    password = PasswordField(label=u'密码', validators=[DataRequired(u'密码不能为空')])
    password2 = PasswordField(label=u'确认密码', validators=[DataRequired(u'确认密码不能为空'), EqualTo("password", u"两次密码不一致")])
    submit = SubmitField(label=u'提交')


@app.route('/register', methods=['POST', 'GET'])
def register():
    # 创建表单对象,如果是post请求，前端发送了数据，flask会把数据
    # 在构造form对象的时候，存放到对象中
    form = Register()
    xx = form.validate_on_submit()
    print(form.user_name)
    # 判断form中的数据是否合理
    # 如果for中的数据完全满足所有的验证器，则返回真，否则返回假
    if form.validate_on_submit():
        # 表示验证合格
        # 提取数据
        user_name = form.user_name.data
        password = form.password.data
        password2 = form.password2.data
        print(user_name, password, password2)
        # 保存了用户的登录信息
        session['username'] = user_name
        return redirect(url_for('index'))
    return render_template('register.html', form=form, xx=xx)


@app.route('/index')
def index():
    return 'index page %s' % session.get('username', '')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
