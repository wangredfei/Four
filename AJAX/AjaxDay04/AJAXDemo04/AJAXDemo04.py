import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/01-server')
def server01():
    return "服务器端已经成功接收异步请求"


@app.route('/02-server')
def server02():
    # 跨域的响应:必须符合JS的语法规范
    # return "console.log('这是02-server动态返回的数据');"

    # 响应给前端:指定前端的哪个方法来执行服务器端响应的内容
    dic = {
        "uname": "Naruto",
        "uage": 16,
        "ugender": "Male",
    }
    jsonStr = json.dumps(dic)

    # aaa({"uname":"Naruto","uage":16,"ugender":"Male"});

    # callback是由前端传递过来的处理响应的函数的名称
    cb = request.args['callback']
    return cb + "(" + jsonStr + ");"


@app.route('/03-flight')
def flight_views():
    dic = {
        'flightNO': 'MM223',
        'start': '北京',
        'to': '上海',
        'date': '17:05',
    }
    jsonStr = json.dumps(dic)
    cb = request.args['callback']
    return cb + "(" + jsonStr + ")"


if __name__ == '__main__':
    app.run(debug=True)
