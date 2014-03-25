import os
import sys
from django.core.urlresolvers import reverse_lazy
from django.conf import global_settings as DEFAULT_SETTINGS


here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Pablo Klijnjan', 'pabloklijnjan@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {}

ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django_browserid.context_processors.browserid',
)

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_browserid.auth.BrowserIDBackend',
)

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = root('..', 'uploads')
MEDIA_URL = ''
STATIC_ROOT = root('..', 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'admin', '/')
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = os.environ.get('SECRET_KEY')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mycarhistory.middleware.xssharing.XsSharingMiddleware',
)

ROOT_URLCONF = 'mycarhistory.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mycarhistory.wsgi.application'

TEMPLATE_DIRS = (
    root('templates'),
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'storages',
    'gunicorn',
    'django_browserid',
    'rest_framework',
    'rest_framework.authtoken',
    'djangosecure',
)

LOCAL_APPS = (
    'mycarhistory.users',
    'mycarhistory.cars',
    'mycarhistory.treatments',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# DRF

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend',
}

# BrowserID

BROWSERID_CREATE_USER = True

# Allow CORS
XS_SHARING_ALLOWED_HEADERS = ['Content-Type', 'Authorization']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': root('..', 'logs', 'mycarhistory.log')
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'mycarhistory': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django_browserid': {
            'handlers': ['logfile', 'console'],
            'level': 'DEBUG',
        }
    }
}
