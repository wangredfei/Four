from flask import Flask

app = Flask(__name__)


# 1.访问路径: /
@app.route('/')
def index():
    return "这是博客的首页"


# 2.访问路径: /list
@app.route('/list')
def list_views():
    return "这是博客的列表页"


# 3.访问路径: /release
@app.route('/release')
def release():
    return "这是博客的发布页面"


# 4.访问路径: /info/id
@app.route('/info/<int:id>')
def info(id):
    return "当前想看id为%d的博客的信息" % id


if __name__ == "__main__":
    app.run(debug=True)
