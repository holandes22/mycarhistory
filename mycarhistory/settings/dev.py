from mycarhistory.settings.base  import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = 'fake'


STATIC_URL = '/static/'

# BrowserID
PERSONA_AUDIENCE = 'http://localhost:8000'

XS_SHARING_ALLOWED_ORIGINS = 'http://localhost:8000'


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
