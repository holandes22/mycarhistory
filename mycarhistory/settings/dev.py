from mycarhistory.settings.base  import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG


STATIC_URL = '/static/'

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

