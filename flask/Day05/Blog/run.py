from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 为app指定配置,配置数据库的连接字符串
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/blog"
# 创建数据库的实例
db = SQLAlchemy(app)


# 创建实例类-User
# id-主键，自增
# uname-用户名(30),唯一,索引
# uemail-邮箱(200)
# url-主站地址，允许为空(200)
# upwd-密码(200)
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30), unique=True, index=True)
    uemail = db.Column(db.String(200))
    url = db.Column(db.String(200), nullable=True)
    upwd = db.Column(db.String(200))
    isActive = db.Column(db.Boolean, default=True)


# 1.访问路径: /
@app.route('/')
def index():
    return render_template('index.html')


# 2.访问路径: /list
@app.route('/list')
def list_views():
    return render_template('list.html')


# 3.访问路径: /release
@app.route('/release')
def release():
    return "这是博客的发布页面"


# 4.访问路径: /info/id
@app.route('/info/<int:id>')
def info(id):
    return "当前想看id为%d的博客的信息" % id


# 5.访问路径 /login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 判断用户的请求意图再决定该响应什么内容
    if request.method == "GET":
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        return "用户名:%s,用户密码:%s" % (username, password)


# 6.访问路径 /register
@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
