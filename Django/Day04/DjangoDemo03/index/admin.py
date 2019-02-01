from django.contrib import admin
from .models import *

#定义高级管理类
class AuthorAdmin(admin.ModelAdmin):
    #1.定义在列表页上所显示的字段们
    list_display = ('name','age','email')
    #2.定义在列表页上能够链接的字段们
    list_display_links = ('name','email')
    #3.定义在列表页上能够被修改的字段们
    list_editable = ('age',)
    #4.定义允许被搜索的字段们
    search_fields = ('name','email')
    #5.定义过滤器实现快速筛选
    list_filter = ('name','email')
    #7.定义详情页中显示的字段以及顺序
    # fields = ('name','email','age')
    #8.定义详情页中的字段分组
    fieldsets = (
        #分组1:组名:基本选项,字段:name,email
        (
            "基本选项",{
                "fields":('name','email'),
            }
        ),
        #分组2:组名:可选选项,字段:age,isActive,可折叠
        (
            "可选选项",{
                "fields":('age','isActive'),
                "classes":('collapse',)
            }
        )
    )

class BookAdmin(admin.ModelAdmin):
    #6.定义时间分层选择器
    date_hierarchy = "publicate_date"

class PublisherAdmin(admin.ModelAdmin):
    #1.列表页:name,city,address
    list_display = ('name','city','address')
    #2.address , city 可编辑
    list_editable = ('address','city')
    #3.过滤器:city
    list_filter = ('city',)
    #4.搜索框:name,website
    search_fields = ('name','website')
    #5.分组:基本信息(name,address,city),高级信息(country,website)
    fieldsets = (
        ("基本信息",{
            "fields":('name','address','city')
        }),
        ("高级信息",{
            "fields":('country','website'),
            "classes":('collapse',)
        })
    )

    pass
# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)
