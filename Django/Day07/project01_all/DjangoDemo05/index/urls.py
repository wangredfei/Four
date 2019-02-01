from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^00-test/$',views.test_views),
    url(r'^01-request/$',views.request_views),
    url(r'^02-post/$',views.post_views),
    url(r'^03-form/$',views.form_views),
    url(r'^04-register/$',views.register_views),
    url(r'^05-login/$',views.login_views),
    url(r'^06-widget01/$',views.widget01),
    url(r'^07-setcookie/$',views.set_cookie),
    url(r'^08-getcookie/$',views.get_cookie),
    url(r'^09-setsession/$',views.set_session),
    url(r'^10-getsession/$',views.get_session),
]

urlpatterns += [
    url(r'^11-ajax-get/$',views.ajax_get),
    url(r'^12-ajax-params/$',views.ajax_params),
    url(r'^13-ajax-post/$',views.ajax_post),
    url(r'^14-ajax-json/$',views.ajax_json),
]







