"""DjangoDemo01 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
import index.views as index_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #localhost:8000/index/xxxx
    # url(r'^index/',include('index.urls')),
    #localhost:8000/music/xxxx
    url(r'^music/',include('music.urls')),

    #　通过主路由配置文件直接进入到应用中的视图处理(跨过应用中的路由)
    #localhost:8000/login
    # url(r'^login/$',index_views.login),
    #localhost:8000/register
    # url(r'^register/$',index_views.register),
    #localhost:8000/
    # url(r'^$',index_views.index),

    #当访问路径不是　admin/xxx , music/xxx 一律要交给index应用中的路由系统去处理
    url(r'^',include('index.urls')),
]
