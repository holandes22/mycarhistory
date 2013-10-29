import dj_database_url
from mycarhistory.settings.base  import *

# Security

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# Allow local dev locally with these settings
# http://stackoverflow.com/questions/14795824/improperlyconfiguredsettings-databases-is-improperly-configured-error-when
DATABASES['default'] =  dj_database_url.config(default='postgres://vagrant:vagrant@localhost/mycarhistory_db')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'mycarhistory'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_URL = 'http://{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SITE_ID = 1
