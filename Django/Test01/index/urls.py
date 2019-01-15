#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # 访问路径是:index/
    url(r'^index/$', views.index),
]
