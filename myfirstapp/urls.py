from django.conf.urls import patterns, url

urlpatterns = patterns('myfirstapp.views',
    url(r'^me/$','hello_world', kwargs={"username":"Mohammed"}, name='hello_me'),
    url(r'^arabizi/(?P<word>\w.)?/?$', 'arabizi', name='arabizi'),
    url(r'^(?P<username>\w+)/$', 'hello_world', name='hello_world'),
)
