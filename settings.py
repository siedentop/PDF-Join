# Django settings for toolsite project.
from default_settings import *

ADMINS = (('Christoph Siedentop', 'christophsiedentop@gmail.com'),
)

MEDIA_ROOT = '/usr/local/django/toolsite/media/'
ADMIN_MEDIA_ROOT = '/usr/local/django/adminmedia'

MEDIA_URL = ''

TEMPLATE_DIRS = (
    "/usr/local/django/toolsite/templates"
)
