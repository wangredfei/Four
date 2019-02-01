from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

#有关用户注册的逻辑处理
def register(request):
    #判断请求方式
    #get:看register.html
    #post:处理请求提交的数据
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        #post请求处理
        #获取uphone的内容,并判断其是否存在
        uphone=request.POST['uphone']
        users=Users.objects.filter(uphone=uphone)
        if users:
            #uphone已经存在
            return render(request,'register.html',{'errMsg':'手机号码已存在'})
        else:
            #将前端数据取出来赋值给users
            users = Users()
            users.uphone = uphone
            users.upwd = request.POST['upwd']
            users.uemail = request.POST['uemail']
            users.uname = request.POST['uname']
            #将users保存进数据库
            #成功去往首页,失败的话则给出提示
            try:
                users.save()
                return redirect('/')
            except Exception as ex:
                print(ex)
                return render(request,'register.html',{'errMsg':'请联系管理员'})








