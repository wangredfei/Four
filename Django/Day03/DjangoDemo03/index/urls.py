from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^01-add-author/$',views.add_author),
    url(r'^02-query/$',views.query),
    url(r'^03-queryall/$',views.queryall),
    url(r'^04-filter/$',views.filter_views),
    url(r'^05-update/(\d+)/$',views.update),
]