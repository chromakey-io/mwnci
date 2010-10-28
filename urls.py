from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/mwnci/media/'}),
    (r'^admin/', include(admin.site.urls)),
    (r'', include('pages.urls')),
)
