from django.conf.urls import url
from shortener import views

urlpatterns = [
    url(r'^short/$', views.short),
    url(r'^([a-z0-9]+)/$', views.myredirect),
]