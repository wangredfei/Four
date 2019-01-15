from flask import Flask, make_response, request, render_template, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'suibianxiesha'


@app.route('/01-addcookie')
def addcookie_views():
    resp = make_response('添加cookie成功')
    resp.set_cookie('uname', 'wangwc', 60 * 60 * 24 * 365)
    return resp


@app.route('/02-getcookie')
def getcookie_views():
    if 'uname' in request.cookies:
        uname = request.cookies.get('uname')
        print('uname的值为:' + uname)
    return "成功获取所有的cookies"


@app.route('/03-register', methods=['GET', 'POST'])
def register_views():
    if request.method == 'GET':
        # 先判断session中是否有登录信息
        if 'uname' in session and 'upwd' in session:
            # session中有登录信息
            uname = session['uname']
            return "欢迎:" + uname
        else:
            # 再判断cookies中是否有uname以及upwd
            if 'uname' in request.cookies and 'upwd' in request.cookies:
                # 获取uname和upwd的值,再进行进一步的判断
                uname = request.cookies['uname']
                upwd = request.cookies['upwd']
                # 再验证uname和upwd是否为admin(或查询数据库)
                if uname == 'admin' and upwd == 'admin':
                    return "您已成功登录过"
                else:
                    return render_template('03-register.html')
            else:
                return render_template('03-register.html')
    else:
        # 1.获取uname和upwd的值
        uname = request.form['uname']
        upwd = request.form['upwd']
        # 2.验证登录是否成功(可以替换为数据库操作)
        if uname == 'admin' and upwd == 'admin':
            # 登录成功
            # 将uname和upwd保存进session中
            session['uname'] = uname
            session['upwd'] = upwd
            resp = make_response('登录成功')
            # 判断是否要保存进cookies
            if 'isSaved' in request.form:
                max_age = 60 * 60 * 24 * 365
                resp.set_cookie('uname', uname, max_age)
                resp.set_cookie('upwd', upwd, max_age)
            return resp
        else:
            # 登录失败
            return render_template('03-register.html', errMsg='用户名或密码不正确')


if __name__ == "__main__":
    app.run(debug=True)
