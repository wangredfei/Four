from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xieshadouxing'


@app.route('/01-addsession')
def addsession_views():
    session['uname'] = 'wangwc'
    session['upwd'] = '123456'
    return "向session中增加数据成功"


@app.route('/02-getsession')
def getsession_views():
    if 'uname' in session and 'upwd' in session:
        uname = session['uname']
        upwd = session['upwd']
        return "session中的数据为,uname:%s,upwd:%s" % (uname, upwd)
    else:
        return "session中没有数据"


if __name__ == "__main__":
    app.run(debug=True)
