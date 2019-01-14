#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 导包
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
# 创建Flask的程序实例
app = Flask(__name__)
# 为Flask的程序实例指定数据库的配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flask'
# 通过Flask的程序实例创建数据库的应用实例
db = SQLAlchemy(app)


@app.route('/')
def index():
    return '程序访问成功'


if __name__ == '__main__':
    app.run(debug=True)
