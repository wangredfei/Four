#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/01-url')
def url_views():
    print(url_for('static', filename='images/2.jpg'))
    return render_template('01-url.html')


@app.route('/02-parent')
def parent_views():
    return render_template('02-parent.html')


@app.route('/03-child')
def child_views():
    return render_template('03-child.html')


@app.route('/04-request')
def request_views():
    print(dir(request))
    return 'Request Success'


@app.route('/05-request')
def request05_views():
    name = request.args['name']
    age = request.args['age']
    return "姓名:%s,年龄:%s" % (name, age)


@app.route('/06-form', methods=['POST', 'GET'])
def form_views():
    if request.method == 'GET':
        # 如果以get方式进入该视图，则渲染06-form.html到客户端浏览器
        return render_template('06-form.html')

    else:
        # 如果以post方式进入到该视图中，则显示提交的数据到终端上
        print(request.form)
        return 'Revieved Message'


if __name__ == '__main__':
    app.run(debug=True)
