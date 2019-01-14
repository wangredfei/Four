# 导包
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 导入pymysql并当成MySQLdb去运行
# import pymysql
# pymysql.install_as_MySQLdb()
# 创建Flask的程序实例
app = Flask(__name__)
# 为Flask的程序实例指定数据库的配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask'
# 为Flask的程序实例指定SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 通过Flask的程序实例创建数据库的应用实例
db = SQLAlchemy(app)


# 创建实体类-Users
# 映射到数据库中表名叫:users
# 创建字段:id,主键，自增
# 创建字段:username,长度为80的字符串，不允许为空，值要唯一
# 创建字段:age,整数，允许为空
# 创建字段:email,长度为200的字符串，唯一
# 创建字段:birth,日期类型
# 创建字段:isActive,布尔类型，默认值为True
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(200), unique=True)
    birth = db.Column(db.Date)
    isActive = db.Column(db.Boolean, default=True)


# 创建Student实体类
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30))
    sage = db.Column(db.SmallInteger)
    isActive = db.Column(db.Boolean, default=True)


# 创建Teacher实体类
class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.BigInteger)


# 创建Course实体类
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(50), nullable=True)


# 将创建好的实体类映射回数据库
db.create_all()


@app.route('/')
def index():
    print(db)  # 能打印输出则说明db创建成功
    return "程序访问成功"


if __name__ == "__main__":
    app.run(debug=True)
