from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^00-test/$',views.test_views),
    url(r'^01-request/$',views.request_views),
    url(r'^02-post/$',views.post_views),
    url(r'^03-form/$',views.form_views),
]