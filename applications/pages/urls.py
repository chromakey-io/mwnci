from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'pages.views.page', name="page"),
    url(r'^(?P<type>[-\w]+)/(?P<path>[-\w]+)/$', 'pages.views.page', name="sub-page"),
    url(r'^(?P<path>[-\w]+)/$', 'pages.views.page', name="page"),
)
