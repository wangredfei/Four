from django.conf.urls import url
from . import views
urlpatterns = [
    #访问路径是: index/
    url(r'^$',views.index),
    #访问路径是: login/
    url(r'^login/$',views.login),
    #访问路径是: register/
    url(r'^register/$',views.register),
]