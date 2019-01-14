from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flask05"
# 配置app的启动模式为调式模式
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# 创建Manager对象并指定要管理哪个应用
manager = Manager(app)
# 创建Migrate对象并指定要关联的app和db
migrate = Migrate(app, db)
# 为manager增加命令,允许做数据表迁移的命令
manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    uage = db.Column(db.Integer)
    uemail = db.Column(db.String(200))

    def __repr__(self):
        return "<User:%r>" % self.uname


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
    tname = db.Column(db.String(30), nullable=True)
    tage = db.Column(db.BigInteger, nullable=False)


# 创建Course实体类
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(50), nullable=True)


@app.route('/')
def index():
    return "This is my first page"


@app.route('/01-adduser')
def addUser_views():
    # 1.创建User的实体对象
    user = User()
    user.uname = 'TeacherWang'
    user.uage = 38
    user.uemail = 'Teacherwang@163.com'
    # 2.通过db.session.add()保存实体对象
    db.session.add(user)
    # 3.提交回数据库
    # db.session.commit()
    return "提交数据成功"


@app.route('/02-query')
def query_views():
    # 1.测试db.session.query()的作用
    # 查询User表中所有的列
    # query=db.session.query(User)
    # 查询User表中id和uname列
    # query=db.session.query(User.id,User.uname)
    # 查询user表和student表中连接后的所有数据
    # query = db.session.query(User,Student)
    # print(type(query))
    # print(query)

    ##################
    ## 2.测试查询执行函数
    ##################

    ##2.1 db.session.query().all()
    ##    查询user表中所有的数据
    # users=db.session.query(User).all()
    # for u in users:
    #     print("id:%d,uname:%s,uage:%d,uemail:%s" % (u.id,u.uname,u.uage,u.uemail))

    ##2.2 查询user表中所有数据的id和uname两个列的值并输出在终端上
    # users=db.session.query(User.id,User.uname).all()
    # for u in users:
    #     print("id:%d,uname:%s" % (u.id,u.uname))

    ##2.3 查询user表中的第一条数据
    # u = db.session.query(User).first()
    # print("id:%d,uname:%s,uage:%d,uemail:%s" % (u.id, u.uname, u.uage, u.uemail))

    ##2.4 查询user表中共有多少条数据
    # count=db.session.query(User).count()
    # print('user表中共有%d条数据' % count)

    ####################
    ## 3. 测试filter()函数
    ####################

    ##3.1 查询年龄大于17的user的信息
    # users=db.session.query(User).filter(User.uage>17).all()
    # print(users)

    ##3.2 查询年龄大于17并且id>1的user的信息
    # query=db.session.query(User).filter(User.uage>17,User.id>1)
    # print(query.all())

    ##3.3 查询年龄大于17或者id大于1的user的信息
    # users=db.session.query(User).filter(or_(User.uage>17,User.id>1)).all()
    # print(users)

    ##3.4 查询uemail中包含rap字符的user的信息
    # users=db.session.query(User).filter(User.uemail.like('%rap%')).all()
    # print(users)

    #######################
    ### 4.测试filter_by()函数
    #######################

    # user=db.session.query(User).filter_by(id=1).first()
    # print(user)

    #######################
    ### 5.测试limit() / offset()函数
    #######################
    # users=db.session.query(User).limit(1).all()
    # print(users)

    # 跳过第一条数据，再获取前一条数据
    # users = db.session.query(User).limit(1).offset(1).all()
    # print(users)

    #######################
    ### 6.测试order_by()函数
    #######################
    users = db.session.query(User).order_by("id desc").all()

    users = db.session.query(User).order_by("uage,id desc").all()
    print(users)

    return "<script>alert('查询成功');</script>"


@app.route('/03-queryall')
def queryall():
    users = db.session.query(User).all()
    return render_template('03-queryall.html', users=users)


if __name__ == "__main__":
    # 通过manager管理启动种程序
    manager.run()
