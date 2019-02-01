from django.conf.urls import url
from . import views
urlpatterns = [
    # 匹配首页
    url(r'^$',views.index),
    # 匹配　login/
    url(r'^login/$',views.login),
    # 匹配　register/
    url(r'^register/$',views.register),
    # 匹配　check_login/
    url(r'^check_login/$',views.check_login),
    # 匹配  type_goods/
    url(r'^type_goods/$',views.type_goods),
]