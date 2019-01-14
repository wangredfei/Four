from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder='temp', static_folder='s', static_url_path="/sta")


@app.route('/01-url')
def url_views():
    print(url_for('static', filename='images/a.jpg'))
    return render_template('01-url.html')


@app.route('/02-parent')
def parent_views():
    return render_template('02-parent.html')


@app.route('/03-child')
def child_views():
    return render_template('03-child.html')


@app.route('/04-request')
def request_views():
    # 查看request对象中的成员
    print(dir(request))
    return "Request Success"


@app.route('/05-request')
def request05_views():
    # print(request.args)
    # name = request.args['name']
    # age = request.args.get('age')
    # return "姓名:%s,年龄:%s" % (name,age)

    # if 'name' in request.args:
    #     name = request.args['name']
    # if 'age' in request.args:
    #     age = request.args['age']
    print('请求方式:' + request.method)
    name = request.args.get('name', '')
    age = request.args.get('age', '0')
    return "姓名:%s,年龄:%s" % (name, age)


@app.route('/06-form', methods=['GET', 'POST'])
def form_views():
    if request.method == 'GET':
        # 如果以get方式进入到该视图中，则渲染06-form.html到客户端浏览器
        return render_template('06-form.html')
    else:
        # 如果以post方式进入到该视图中，则显示提交的数据们到终端上
        print(request.form)
        name = request.form['name']
        age = request.form['age']
        print("姓名:%s,年龄:%s" % (name, age))
        return "Revieved Message"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
