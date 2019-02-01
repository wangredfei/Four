from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def test_views(request):
    return HttpResponse("<a href='/01-request/'>测试的链接</a>")

def request_views(request):
    # print(dir(request))
    print("request.scheme:%s" % request.scheme)
    print("request.path:%s" % request.path)
    print("request.method:%s" % request.method)
    print("request.GET:",request.GET)
    print("request.POST:",request.POST)
    print("request.COOKIES:",request.COOKIES)
    print("request.META:",request.META)
    #判断有没有请求的源地址
    if 'HTTP_REFERER' in request.META:
        print('请求源地址:',request.META['HTTP_REFERER'])
    else:
        print('没有请求源地址')
    return HttpResponse("请求对象获取成功")

def post_views(request):
    # 判断请求方式,
    # 如果是get则去往02-post.html
    # 如果是post则接收请求提交的数据
    if request.method == 'GET':
        return render(request,'02-post.html')
    else:
        #接收前端传递过来的uname和upwd
        uname=request.POST.get('uname')
        upwd = request.POST.get('upwd')
        return HttpResponse("用户名称:%s,用户密码:%s" % (uname,upwd))


def form_views(request):
    if request.method == 'GET':
        #创建RemarkForm的对象,并发送到03-form.html上
        form = RemarkForm()
        return render(request,'03-form.html',locals())
    else:
        #通过forms模块来获取提交的数据
        #1.将提交的数据给RemarkForm()
        form = RemarkForm(request.POST)
        #2.通过验证
        if form.is_valid():
            #3.取值
            cd = form.cleaned_data
            print(cd)
            return HttpResponse("取值成功")
        return HttpResponse("取值失败")

def register_views(request):
    if request.method == 'GET':
        # 使用自定义form类
        # form = RegisterForm()
        # 使用与Models相关联的form类
        form = ModelRegisterForm()
        return render(request,'04-register.html',locals())
    else:
        #1.将request.POST给RegisterForm()
        #form = RegisterForm(request.POST)

        #将request.POST给ModelRegisterForm()
        form = ModelRegisterForm(request.POST)
        #2.判断是否通过验证
        if form.is_valid():
            #3.通过验证后,获取数据并构建成Users的对象
            user = Users(**form.cleaned_data)
            #4.将Users的对象保存回数据库
            user.save()
            return HttpResponse('注册成功')
        return HttpResponse("数据有误,注册失败")

def login_views(request):
    if request.method == 'GET':
        form = ModelLoginForm()
        return render(request,'05-login.html',locals())
    else:
        uname=request.POST['uname']
        upwd = request.POST['upwd']
        users = Users.objects.filter(uname=uname,upwd=upwd)
        if users:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("登录失败")

def widget01(request):
    form = WidgetRegisterForm()
    return render(request,'06-widget01.html',locals())


def set_cookie(request):
    resp = HttpResponse("成功响应数据到客户端")
    expires = 60*60*24*365
    resp.set_cookie('USERID','66998877',expires)
    return resp

def get_cookie(request):
    # print(request.COOKIES)
    if 'USERID' in request.COOKIES:
        print('userid的值为:'+request.COOKIES['USERID'])
    return HttpResponse("获取cookie成功")

def set_session(request):
    request.session['USERID'] = '66997788'
    request.session['UNAME'] = 'lixiaochao'
    return HttpResponse('session数据保存成功')

def get_session(request):
    uid=request.session['USERID']
    uname=request.session['UNAME']
    return HttpResponse("UID:%s,UNAME:%s" % (uid,uname))


