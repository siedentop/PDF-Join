# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'pdfjoin.views.show_start', name='pdfjoin'),
)
