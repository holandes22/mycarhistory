from mycarhistory.settings.base  import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = 'fake'


STATIC_URL = '/static/'

# BrowserID
PERSONA_AUDIENCES = (
    'http://localhost:8000',
    'https://localhost:8000',
    'http://127.0.0.1:8000',
    'https://127.0.0.1:8000',
    'http://localhost:4200',
    'https://localhost:4200',
    'http://127.0.0.1:4200',
    'https://127.0.0.1:4200',
)

XS_SHARING_ALLOWED_ORIGINS = 'http://localhost:4200'


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
