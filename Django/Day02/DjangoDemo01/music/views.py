from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("这是music应用中的index访问路径")

def template_views(request):
    #1.通过loader加载模板
    # t = loader.get_template('01-template.html')
    #2.将模板转换成字符串
    # html = t.render()
    #3.将字符串响应给客户端
    # return HttpResponse(html)

    #2.使用render直接加载并响应模板
    return render(request,'01-template.html')

def var_views(request):
    uname = "wangwc"
    uage = 37
    list = ["王老师","王夫人","李小超"]
    dic = {
        "SWK":"孙悟空",
        "ZWN":"猪无能",
        "WWC":"王伟超",
    }
    person = Person()
    person.uname = "哲学吕"

    return render(request,'02-var.html',locals())

def static_views(request):
    return render(request,'03-static.html')

def parent(request):
    return render(request,'04-parent.html')

def child(request):
    return render(request,'05-child.html')

def test_views(request):
    return HttpResponse("<h1>this is test views</h1>")

def reg_views(request,num):
    return HttpResponse("<h1>传递过来的值为:%s</h1>" % num)










class Person(object):
    uname = None
    def intro(self):
        return "Hello,my name is %s " % self.uname





