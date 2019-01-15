from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def music(request):
    return HttpResponse("这是music应用中的show访问路径")


def template_views(request):
    # 1.通过loader加载模板
    # t = loader.get_template('01-template.html')
    # 2.将模板转换成字符串
    # html = t.render()
    # 3.将字符串响应给客户端
    return render(request, '01-template.html')


def var_views(request):
    uname = 'wangwc'
    uage = 37
    list = ["王老师", "王夫人", "李小草"]
    dic = {
        "SWK": "孙悟空",
        "ZWN": "猪悟能",
        "WWC": "王伟超",
    }
    person = Person()
    person.uname = "哲学吕"
    return render(request, '02-var.html', locals())


class Person(object):
    uname = None

    def intro(self):
        return "Hello World,This is %s" % self.uname


def static_views(request):
    return render(request, '03-static.html')


def parent(request):
    return render(request, '04-parent.html')


def child(request):
    return render(request, '05-child.html')
