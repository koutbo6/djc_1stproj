from django.conf.urls import patterns, url
from myfirstapp import views

urlpatterns = [
    url(r'^me/$',views.hello_world, kwargs={"username":"Mohammed"}, name='hello_me'),
    url(r'^arabizi/(?P<word>\w.)?/?$', views.arabizi, name='arabizi'),
    url(r'^(?P<username>\w+)/$', views.hello_world, name='hello_world'),
]
