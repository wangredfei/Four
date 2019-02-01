from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:123456@localhost:3306/flaskLogin"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DEBUG']=True
app.config['SECRET_KEY']='you guess'
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer,primary_key=True)
    uname=db.Column(db.String(30))
    upwd=db.Column(db.String(200))
    nickname=db.Column(db.String(50))

    def __init__(self,uname,upwd,nickname):
        self.uname = uname
        self.upwd = upwd
        self.nickname = nickname

@app.route('/01-register',methods=['GET','POST'])
def register_views():
    if request.method == 'GET':
        return render_template("01-register.html")
    else:
        uname = request.form['uname']
        upwd = request.form['upwd']
        nickname = request.form['nickname']
        #使用generate_password_hash()对upwd进行加密，并接收加密后的结果
        upwd = generate_password_hash(upwd)
        user=User(uname,upwd,nickname)
        db.session.add(user)
        #将数据保存进session即可
        session['uname']=uname
        return redirect('/')

@app.route('/')
def index_views():
    #判断session中是否有uname的值
    if 'uname' in session:
        uname = session.get('uname')
        user = User.query.filter_by(uname=uname).first()
    return render_template('index.html',params=locals())

@app.route('/logout')
def logout_views():
    url = request.headers.get('Referer','/')
    resp = redirect(url)
    #判断session中是否有uname,如果有的话则清空
    if 'uname' in session:
        del session['uname']
    #判断cookie中是否有uname的值,如果有的话则清空
    if 'uname' in request.cookies:
        resp.delete_cookie('uname')
    #返回到 "从哪来回哪去,不知道从哪来则回首页"
    return resp

@app.route('/login',methods=['POST','GET'])
def login_views():
    if request.method == 'GET':
        #获取请求源地址，并存放进session，如果没有请求源地址，则将 / 保存进session
        url=request.headers.get('Referer','/')
        session['url'] = url

        #判断session中是否有uname的值
        if 'uname' in session:
            #有uname,从哪来回哪去
            return redirect(url)
        else:
            #session中没有对应的数据
            #继续判断cookie(之前有没有保存过密码)
            if 'uname' in request.cookies:
                #cookie中有登录信息(保存过密码)
                #取出uname的值,并且判断正确性
                uname=request.cookies['uname']
                user=User.query.filter_by(uname=uname).first()
                #判断user是否为空
                if user:
                    #说明uname是正确的，则保存进session
                    session['uname'] = uname
                    return redirect(url)
            #     else:
            #         #说明uname不正确需要重新登录
            #         return render_template('login.html')
            # else:
            #     #之前没保存过密码
            #     return render_template('login.html')
            return render_template('login.html')
    else:
        #接收前端传递过来的用户名和密码
        uname = request.form['uname']
        upwd = request.form['upwd']
        #验证用户名和密码是否正确
        user=User.query.filter_by(uname=uname).first()
        if user and check_password_hash(user.upwd,upwd):
            #登录成功
            #将uname的值保存进session
            session['uname']=uname
            #从session中获取url，并构建响应对象
            url=session.get('url','/')
            resp = redirect(url)
            #判断是否要存cookie
            if 'isSaved' in request.form:
                resp.set_cookie('uname',uname,60*60*24*365*10)
            return resp

        else:
            #登录失败
            return render_template('login.html',errMsg='用户名或密码不正确')

if __name__ == "__main__":
    manager.run()