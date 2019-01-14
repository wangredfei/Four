#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list')
def list_views():
    return render_template('list.html')


@app.route('/release')
def release():
    return '这是博客的发布页面'


@app.route('/info/<int:id>')
def info(id):
    return '当前想看的id为%d的博客信息' % id


# 5.访问路径/login
@app.route('/login')
def login():
    return render_template('login.html')


# 6.访问路径 /register
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/list')
def list():
    return render_template('list.html')


if __name__ == '__main__':
    app.run(debug=True)
