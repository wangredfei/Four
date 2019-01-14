from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, func

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
    # 增加一个属性-isActive,默认值为True
    isActive = db.Column(db.Boolean, default=True)

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
    # 增加对Course(一)类的引用
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))


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


@app.route('/04-update', methods=['GET', 'POST'])
def update_views():
    if request.method == 'GET':
        # 先获取提交过来的参数
        id = request.args['id']
        # 再根据参数查询对应的用户的信息
        user = db.session.query(User).filter_by(id=id).first()
        # 伴随着响应将用户信息渲染给04-update.html
        return render_template('04-update.html', user=user)
    else:
        # 接收提交过来的要修改的数据
        id = request.form['id']
        uname = request.form['uname']
        uage = request.form['uage']
        uemail = request.form['uemail']
        # 根据id查询要修改的实体
        user = User.query.filter_by(id=id).first()
        # 给实体赋值
        user.uname = uname
        user.uage = uage
        user.uemail = uemail
        # 再更新回数据库
        db.session.add(user)
        # 响应
        # return queryall()
        # 　将请求重定向到 /03-queryall 地址上
        # 可以使用 redirect('地址') 函数完成上述功能
        return redirect('/03-queryall')


@app.route('/05-query')
def query05_views():
    #####################
    ## 1.聚合函数的使用
    ####################

    ## 1.1 查询user表中所有人的平均年龄
    # result = db.session.query(func.avg(User.uage)).first()
    # print(result[0])

    ## 1.2 按user表中的uage列进行分组,求每组中的uage的平均值,以及uage的总和
    # result=db.session.query(
    #     User.uage,
    #     func.avg(User.uage),
    #     func.sum(User.uage)
    # ).group_by('uage').all()
    # # print(result)
    # for r in result:
    #     print('组:',r[0],',平均年龄:',r[1],',总年龄:',r[2])

    ##1.3 查询被激活和未被激活的用户的数量
    # result=db.session.query(
    #     User.isActive,
    #     func.count(User.isActive)
    # ).group_by('isActive').all()
    #
    # for r in result:
    #     print(r[0],'的数量为:',r[1])

    ##1.4　查询年龄>16的user们激活和未被激活的人数，并且将人数大于2人的信息输出
    result = db.session.query(User.isActive, func.count(User.isActive)).filter(User.uage > 16).group_by(
        'isActive').having(func.count(User.isActive) > 2).all()
    print(result)

    return "<script>alert('查询成功');</script>"


@app.route('/06-update')
def update06_views():
    # 修改id为4的用户的信息
    user = User.query.filter_by(id=4).first()
    user.uname = 'Zhexue LV'
    user.uage = 30
    user.uemail = "lvze@163.com"
    user.isActive = True
    db.session.add(user)
    return "修改成功"


@app.route('/07-delete')
def delete_views():
    # 1.先获取传递过来的id
    id = request.args['id']
    # 2.查询指定id值的user的信息
    user = User.query.filter_by(id=id).first()
    # 3.通过db.session.delete()删除指定用户
    db.session.delete(user)
    # 4.响应:重定向到/03-queryall
    return redirect('/03-queryall')


if __name__ == "__main__":
    # 通过manager管理启动种程序
    manager.run()
