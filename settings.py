# Django settings for toolsite project.
from default_settings import *

DEBUG = True

ADMINS = (
   ('Christoph Siedentop', 'christophsiedentop@gmail.com'),
)
MEDIA_ROOT = '/home/chris/devel/toolsite/media'

MEDIA_URL = ''

TEMPLATE_DIRS = (
    "/usr/local/django/toolsite/templates"
)

CSRF_FAILURE_VIEW = (
	'pdfjoin.views.csrf_failure'
)
