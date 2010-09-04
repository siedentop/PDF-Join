import os, sys

sys.path.append('/usr/local/django')
sys.path.append('/usr/local/django/toolsite')
sys.path.append('/usr/local/django/toolsite/pyPdf')

os.environ['DJANGO_SETTINGS_MODULE'] = 'toolsite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
