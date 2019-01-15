#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

# 进入到此urls.py中说明已经匹配上了localhost:8000/music/
# 所以在此文件中只需要匹配具体的资源路径就可以了


urlpatterns = [
    # 完整的请求路径是:localhost:8000/music/show/
    url(r'music/$', views.music),

    # 访问路径是01-template/ 交给template_views处理
    url(r'^01-template/$', views.template_views),

    url(r'^02-var/$', views.var_views),

    url(r'^03-static/', views.static_views),

    url(r'^04-parent/$', views.parent),
    url(r'^05-child/$', views.child),
]
