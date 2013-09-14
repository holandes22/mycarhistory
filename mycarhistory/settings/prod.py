import dj_database_url
from carlogger.settings.base  import *

# Allow local dev locally with these settings
# http://stackoverflow.com/questions/14795824/improperlyconfiguredsettings-databases-is-improperly-configured-error-when
DATABASES['default'] =  dj_database_url.config(default='postgres://vagrant:vagrant@localhost/carlogger_db')

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SITE_ID = 1
