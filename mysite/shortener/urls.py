from django.conf.urls import url
from shortener import views

urlpatterns = [
    url(r'^short-form/$', views.make_short),
    url(r'^short/$', views.short),
    url(r'^(\d+)/$', views.myredirect),
]