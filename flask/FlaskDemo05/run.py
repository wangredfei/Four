#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.43.129:3306/flask05'
# 配置app的启动模式为调试模式
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 创建Manger对象并指定要管理那个应用
manager = Manager(app)
# 创建Ｍigrate对象并指定要关联的app和db
migrate = Migrate(app, db)
# 为manager增加命令，允许数据表迁移的命令
manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    uage = db.Column(db.Integer)
    uemail = db.Column(db.String(20))


@app.route('/')
def index():
    return 'This is my first page'


if __name__ == '__main__':
    # 通过manager管理启动程序
    manager.run()
