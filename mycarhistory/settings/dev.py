from mycarhistory.settings.base  import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG


STATIC_URL = '/static/'

# BrowserID
SITE_URL = ['http://localhost:8888', 'http://127.0.0.1:8888']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mycarhistory_db',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': '',
        'PORT': '',
    }
}
