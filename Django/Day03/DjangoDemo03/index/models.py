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
#Author - 作者
#name - models.CharField()
#age - models.IntegerField()
#email - models.EmailField()
class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    #增加isActive表示是否处于启用状态-models.Boolean
    isActive = models.BooleanField(default=True)

#Book - 书籍
#title - models.CharField()
#publicate_date - models.DateField()
class Book(models.Model):
    title = models.CharField(max_length=30)
    publicate_date = models.DateField()






