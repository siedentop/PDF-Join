from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	(r'^admin/', include(admin.site.urls)),

	(r'^$', direct_to_template,  { 'template': 'index.html' }, 'index'),

	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	
	(r'^pdfjoin/', include('pdfjoin.urls')),
)
