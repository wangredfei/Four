from flask import Flask, request

app = Flask(__name__)

@app.route('/02-server')
def server02_views():
    return "这是我的第一个ajax的响应"

@app.route('/03-server')
def server03_views():
    #接收前端传递过来的数据
    uname=request.args['uname']
    return "欢迎:"+uname

if __name__ == "__main__":
    app.run(debug=True)