from flask import Flask, render_template

app = Flask(__name__)


@app.route('/01-selftemp')
def selftemp():
    html = "<!doctype html>"
    html += "<html>"
    html += "<head>"
    html += "<title>我自己的模板</title>"
    html += "</head>"
    html += "<body>"
    html += "<h1>这是我的第一个自己的模板</h1>"
    html += "</body>"
    html += "</html>"
    return html


@app.route('/02-template')
def template_views():
    ret = render_template('02-temp.html', name='wangwc', age=35, gender='男')
    print(ret)
    return ret


@app.route('/03-template')
def template03():
    title = '绿光'
    author = '宝强'
    music = '乃亮'
    singer = '羽凡'
    date = '2015-10-15'
    # print(locals())
    return render_template('03-template.html', params=locals())


@app.route('/04-var')
def var():
    ustr = '这是,一段我要,测试的包含中文的内容'
    name = '王者荣耀'
    delay = 460
    list = ['阿珂', '兰陵王', '孙悟空', '李白']
    tup = ('蔡文姬', '名师因', '刘禅')
    dic = {
        'AQL': '安其拉',
        'DJ': '妲己',
        'WZJ': '王昭君'
    }
    game = Game()
    game.group = '深渊大乱斗'
    print(locals())
    return render_template('04-var.html', params=locals())


@app.route('/05-macro')
def macro_views():
    list = ['孙悟空', '西门庆', '小乔', '刘姥姥']
    return render_template('05-macro.html', list=list)


class Game(object):
    group = None

    def prt(self):
        return "测试的内容：" + self.group


if __name__ == "__main__":
    app.run(debug=True)
