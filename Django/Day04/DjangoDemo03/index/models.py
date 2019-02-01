from django.db import models

# Create your models here.
#创建一个实体类-Publisher
#表示出版社信息,属性如下:
#1.name:出版社名称(varchar)
#2.address:出版社所在地址(varchar)
#3.city:出版社所在城市(varchar)
#4.country:出版社所在国家(varchar)
#5.website:出版社网址(varchar)
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return self.name

#Author - 作者
#name - models.CharField()
#age - models.IntegerField()
#email - models.EmailField()
class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='邮箱')
    #增加isActive表示是否处于启用状态-models.Boolean
    isActive = models.BooleanField(default=True,verbose_name='活动用户')

    #通过　__str__ 修改展现形式
    def __str__(self):
        return self.name

    #定义内部类-Meta
    class Meta:
        #1.指定表名
        db_table = 'author'
        #2.指定后台展现名称(单数)
        verbose_name = '作者'
        #3.指定后台展现名称(复数)
        verbose_name_plural = verbose_name
        #4.指定排序
        ordering = ["age","-id"]


#Book - 书籍
#title - models.CharField()
#publicate_date - models.DateField()
class Book(models.Model):
    title = models.CharField(max_length=30)
    publicate_date = models.DateField()
    #增加对Publisher(一)的引用关系
    publisher = models.ForeignKey(Publisher,null=True,verbose_name='出版社')
    #增加对Author(多)的引用关系
    author_set = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

#Wife - 夫人
#name,age
class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    #增加属性-author,表示与Author表的一对一关系
    author = models.OneToOneField(Author,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name = '夫人'
        verbose_name_plural = verbose_name




