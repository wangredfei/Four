#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # 匹配首页
    url(r'^$', views.index),
    # 匹配 login/
    url(r'^login/$', views.login),
    url(r'^register/$',views.register),
]
