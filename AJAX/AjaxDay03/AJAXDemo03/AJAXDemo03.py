import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flaskLogin"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    upwd = db.Column(db.String(200))
    nickname = db.Column(db.String(50))

    def to_dict(self):
        dic = {
            'id': self.id,
            'uname': self.uname,
            'upwd': self.upwd,
            'nickname': self.nickname
        }
        return dic


class Province(db.Model):
    __tablename__ = "province"
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(30))
    # 增加关联属性和反向引用关系属性
    cities = db.relationship("City", backref='province', lazy="dynamic")

    def to_dict(self):
        dic = {
            'id': self.id,
            'pname': self.pname
        }
        return dic


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30))
    pid = db.Column(db.Integer, db.ForeignKey('province.id'))


db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/01-load', methods=['GET', 'POST'])
def load_views():
    # name=request.args['name']
    # age=request.args['age']

    name = request.form['name']
    age = request.form['age']
    # return "这是使用load方法加载回来的数据"
    return "姓名:%s,年龄:%s" % (name, age)


@app.route('/03-server')
def server03():
    # uname = request.args['uname']
    # uage = request.args['uage']
    # return "接收到的数据为uname=%s,uage=%s" % (uname,uage)

    ##查询user表中所有的数据并以json的格式进行响应
    users = User.query.all()
    list = []
    for u in users:
        list.append(u.to_dict())
    return json.dumps(list)


@app.route('/04-search')
def search_views():
    # 接收前端传递过来的参数-get方式
    uname = request.args['uname']
    # 模糊查询:user表中uname字段里包含uname字符的所有的数据
    users = User.query.filter(User.uname.like('%' + uname + '%')).all()
    # 声明一个空列表,将users中的每个数据都转换成字典并追加到列表中
    list = []
    for u in users:
        list.append(u.to_dict())
    return json.dumps(list)


@app.route('/05-loadpro')
def loadpro_views():
    # 获取province表中所有的数据,并构建成json字符串响应
    provinces = Province.query.all()
    list = []
    for pro in provinces:
        list.append(pro.to_dict())
    return json.dumps(list)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
