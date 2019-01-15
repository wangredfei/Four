#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.http import HttpResponse


# Django 中的视图处理函数中必须要有一个参数,名称必须叫request
def show(request):
    return HttpResponse('我的第一个Django程序')


def show_02(request, year, month, day):
    # 参数year表示地址中的四位整数
    return HttpResponse("生日:%s年%s月%s日" % (year, month, day))


def music(request):
    return '这是music程序'
