from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def add_author(request):
    #使用Entry.objects.create()实现增加数据
    # author=Author.objects.create(name='莫言',age=65,email='moyan@163.com')
    # print(author)

    #创建Entry的对象，并调用其save()
    # author = Author(name='鲁迅',age=95)
    # author.email = 'zhoushuren@163.com'
    # author.save()

    #使用字典创建对象,并调用其save()
    dic = {
        'name':'巴金',
        'age' : 100,
        'email': 'eightJin@163.com',
        'isActive' : False,
    }
    author = Author(**dic)
    author.save()
    print('ID:'+str(author.id))
    print('Name:'+author.name)
    print('Age:'+str(author.age))
    print('Email:'+author.email)
    print('isActive:'+str(author.isActive))
    return HttpResponse("<script>alert('增加数据成功');</script>")


def query(request):
    ###############
    ###1.all()
    ##############
    # authors=Author.objects.all()
    # print(authors.query)
    # print(authors)
    #循环遍历authors每条数据
    # for au in authors:
    #     print("ID:%d,Name:%s,Age:%s" % (au.id,au.name,au.age))

    ################################
    ######  2.values()   ###########
    ################################
    # authors=Author.objects.values()
    authors=Author.objects.values('id','email')
    print(authors)
    # for au in authors:
    #     print('ID:%d,Name:%s' % (au['id'],au['name']))


    return HttpResponse("<script>alert('查询数据成功');</script>")

def queryall(request):
    #1.查询Author中的所数据
    authors = Author.objects.all()
    #2.将查询结果渲染到03-queryall.html
    return render(request,'03-queryall.html',locals())


def filter_views(request):
    #1.查询id为1的Author的信息
    # authors=Author.objects.filter(id=1).values('name')
    # print(authors.query)
    # print(authors)

    #2.查询id为1并且name为莫言的Author的信息
    # authors=Author.objects.filter(id=1,name='莫言')
    # print(authors.query)
    # print(authors)

    # 查询谓词
    # 1.查询　age>=95的Author的信息
    # authors=Author.objects.filter(age__gte=95).values()
    # print(authors)

    #2.查询所有姓鲁
    # authors=Author.objects.filter(name__startswith='鲁').values()

    #3.查询Email中包含'sh'字符
    # author=Author.objects.filter(email__contains='sh')

    #4.查询年纪大于鲁迅的年纪的人的信息
    # authors=Author.objects.filter(
    #     age__gt=(
    #         Author.objects.filter(
    #             name='鲁迅'
    #         ).values('age')
    #     )
    # ).values('name','age')
    # print(authors)


    ###不等条件查询-exclude
    #1.查询id不等于1的所有的Author的信息
    # authors=Author.objects.exclude(id=1)
    # print(authors.query)
    # print(authors.values('name','age'))
    #2.查询年龄不大于100的Author的信息
    authors = Author.objects.exclude(age__gt=100).values('name','age')
    print(authors.query)
    print(authors)

    return HttpResponse("Query OK")

def update(request,id):
    #1.根据id查询出对应的Author的信息
    author=Author.objects.get(id=id)
    print(author)
    #2.将Author的信息渲染到05-update.html模板
    return render(request,'05-update.html',locals())