from flask import Flask, request, render_template
from flask_mail import Mail, Message
from flask_script import Manager

# 创建应用
app = Flask(__name__)

# # 配置信息
# class Config(object):
#     DEBUG = True,
#     MAIL_SERVER = 'smtp.qq.com',
#     MAIL_PROT = 25,
#     MAIL_USE_TLS = True,
#     MAIL_USERNAME = '1486504210@qq.com',
#     MAIL_PASSWORD = 'xqdukjqvgppljdje',
#
#
# # 加载配置
# app.config.from_object(Config)
# 配置邮件：服务器／端口／传输层安全协议／邮箱名／密码
# 必须得通过字典的方式加入，通过对象无法被Mail读取到
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=25,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='1486504210@qq.com',
    MAIL_PASSWORD='xqdukjqvgppljdje',
)
# 创建manager管理app
manager = Manager(app)

# 创建mail,因为要读取app里面的配置信息，所以app做参数
mail = Mail(app)


# 创建试图函数
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # 接受收件人邮件
        receive_email = request.form.get('email')
        print(receive_email)

        # 组织消息体
        msg = Message("This is a test ",
                      sender=app.config.get('MAIL_USERNAME'),
                      recipients=[receive_email]
                      )
        # 邮件内容
        msg.body = "Flask test mail"
        # 发送邮件
        mail.send(msg)
        return 'ok'
    return render_template('send_mail.html')


if __name__ == '__main__':
    manager.run()
