from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Sum,Avg,Count

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
    # authors = Author.objects.all()
    #1.查询出isActive为True的信息
    authors = Author.objects.filter(isActive=True)
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

def aggregate(request):
    #1.查询Author表中所有人的年纪总和
    # result = Author.objects.aggregate(sumAge=Sum('age'))
    # print('年纪总和为:%d' % (result['sumAge']))
    #2.查询Author表中所有人的平均年龄以及总年龄
    result = Author.objects.aggregate(avgAge=Avg('age'),sumAge=Sum('age'))
    print(result)
    #3.查询Author表中年纪>=90的人的数量
    result = Author.objects.filter(age__gte=90).aggregate(count=Count('age'))
    print(result)
    return HttpResponse("Query OK")

def annotate(request):
    #按isActive进行分组，求每组的人数
    result=Author.objects.values('isActive').annotate(count=Count('*')).values('count')
    print(result)
    return HttpResponse("Query OK")

def update08(request):
    #1.获取'巴金'
    # au = Author.objects.get(name='巴金')
    #2.修改其email的值
    # au.email = 'bajin@163.com'
    #3.保存回数据库
    # au.save()

    #修改所有人的isActive的值为True
    Author.objects.all().update(isActive=True)
    return HttpResponse('更新成功')

def delete(request,id):
    #1.根据id查询出对应的Author的信息
    au = Author.objects.get(id=id)
    #2.将其的isActive的值修改为False
    au.isActive = False
    #3.再保存回数据库
    au.save()
    #4.响应:重定向回/03-queryall
    return redirect('/03-queryall')

def oto_views(request):
    #创建一个　wife 对象并指定author信息再保存回数据库
    # 方式1:通过author_id关联
    # wife = Wife()
    # wife.name = '莫夫人'
    # wife.age = 50
    # wife.author_id = 1
    # wife.save()

    #方式2:通过author关联
    # author=Author.objects.get(name='巴金')
    # wife = Wife()
    # wife.name = '巴夫人'
    # wife.age = 96
    # wife.author = author
    # wife.save()

    # 查询
    # 通过Author查询Wife
    # author = Author.objects.get(name='巴金')
    # wife = author.wife
    # print("作者姓名:%s,年龄:%d" % (author.name,author.age))
    # print("夫人姓名:%s,年龄:%d" % (wife.name,wife.age))
    # 通过Wife查询Author
    wife = Wife.objects.get(id=1)
    author = wife.author
    print("夫人姓名:%s,年龄:%d" % (wife.name, wife.age))
    print("作者姓名:%s,年龄:%d" % (author.name, author.age))
    return HttpResponse('查询成功')


def otm_views(request):
    #正向查询 - 通过Book查询对应的Publisher
    # 查询id为3的书籍信息
    book = Book.objects.get(id=3)
    # 查询对应的出版社
    publisher = book.publisher
    #反向查询 - 通过Publisher查询对应的所有的Book
    # 查询北京大学出版社的信息
    pub = Publisher.objects.get(name='北京大学出版社')
    # 查询对应的所有的书籍 - book_set
    books = pub.book_set.all()
    return render(request,'11-otm.html',locals())


def mtm_views(request):
    #增加数据:为Book绑定Author
    #查询Book-"射雕英雄传"
    # book = Book.objects.get(title='射雕英雄传')
    #查询Author-金庸
    # author = Author.objects.get(name='金庸')
    #关联Book和Author(如果插入多条关联数据,使用列表)
    # book.author_set.add(author)
    #通过Book的author_set的remove()删除author的关联信息
    # book.author_set.remove(author)

    # 正向查询 - 通过Book查询Author
    # 查询Book - 碧血剑
    book=Book.objects.get(title='碧血剑')
    # 获取对应的所有的Author
    authors = book.author_set.all()

    # 反向查询-通过Author查找Book
    # 查询Author - 金庸
    au = Author.objects.get(name='金庸')
    # 获取对应所出版的书籍
    books = au.book_set.all()
    return render(request,'12-mtm.html',locals())








