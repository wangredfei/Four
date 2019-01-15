"""Test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 当我的访问路径是 show/ 的时候,交给views.show()去处理请求和响应
    url(r'^show/$', views.show),
    # 传递四位整数
    url(r'^show_02/(\d{4})/(\d{2})/(\d{2})/$', views.show_02),
    # url(r'^music/',include('music.urls')),

]

urlpatterns += [
    # 当访问路径是localhost:8000/music/xxx的时候,要将地址交给music的urls进一步处理
    url(r'^music/', include('music.urls')),
    # url(r'^index/$',include('index.urls'))
]
