from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^01-add-author/$',views.add_author),
    url(r'^02-query/$',views.query),
    url(r'^03-queryall/$',views.queryall),
    url(r'^04-filter/$',views.filter_views),
    url(r'^05-update/(\d+)/$',views.update),
    url(r'^06-aggregate/$',views.aggregate),
    url(r'^07-annotate/$',views.annotate),
    url(r'^08-update/$',views.update08),
    url(r'^09-delete/(\d+)/$',views.delete),
]

urlpatterns += [
    url(r'^10-oto/$',views.oto_views),
    url(r'^11-otm/$',views.otm_views),
    url(r'^12-mtm/$',views.mtm_views),
]