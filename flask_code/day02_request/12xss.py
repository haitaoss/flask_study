# coding:utf-8

from flask import Flask, render_template, request

# 创建flask应用
app = Flask(__name__)




# 视图函数
@app.route('/xss', methods=['POST', 'GET'])
def xss():
    text = ""
    if request.method == 'POST':
        text = request.form.get('text')
    return render_template('xss.html', text=text)


# 启动flas应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # manager.run()
