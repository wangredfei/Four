from flask import Flask, render_template

app = Flask(__name__)


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
@app.route('/login')
def login():
    return render_template('login.html')


# 6.访问路径 /register
@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
