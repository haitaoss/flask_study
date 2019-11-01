# coding:utf-8
from flask import Flask, render_template, flash

app = Flask(__name__)

# 设置秘钥
app.config['SECRET_KEY'] = 'sfaufhdioa23749328sdjnfajk'
#
flag = True


@app.route('/index')
def index():
    if flag:
        # 添加闪现信息
        flash('hello1')
        flash('hello2')
        flash('hello3')
        global flag
        flag = False
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
