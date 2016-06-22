"""
Django settings for uopy project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging
import os
import re
import json

logging.log(logging.INFO, 'loading settings for ' + __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0h6urdfl%-bs=mc!%&ybj@=8a4rrqc^26t!6738*nf!l2ut8k#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Application definition


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
)

#CACHE_BACKEND = 'db://hello.sqlite3'
#CACHE_BACKEND = os.path.join(BASE_DIR, 'hello.txt')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

ROOT_URLCONF = 'uopy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',

            ],
        },
    },
]

WSGI_APPLICATION = 'uopy.wsgi.application'

IGNORABLE_404_URLS = (
    re.compile(r'\.(php|cgi)$'),
    re.compile(r'^/phpmyadmin/'),
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

FILE_UPLOAD_PERMISSIONS = 0o644

SESSION_COOKIE_AGE = 3600
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True


#easy thumbnails settings
THUMBNAIL_ALIASES = {
        'mini': {'size': (50, 50), 'crop': False},
        'medio': {'size': (300, 300), 'crop': False},
}
DEFAULT_MASCOTA_IMAGE_SETTING = THUMBNAIL_ALIASES['medio']


# LOGGING
LOGGING = {
     'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s %(funcName)s %(lineno)d %(message)s'
        },
        'normal': {
            'format': '%(levelname)s %(asctime)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
     },
     'handlers': {
         'file': {
             'level': 'INFO',
             'class': 'logging.FileHandler',
             'formatter': 'verbose',
             'filename': BASE_DIR+'/logs/dev.log',
             'mode': 'a',
         },
     },
     'loggers': {
         'django': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
         'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
         'applications.events.views': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
          'applications.events.models': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
         '': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
     },
 }


gettext = lambda x: x

LANGUAGES = (
   ('fr', gettext('French')),
   ('en', gettext('English')),
   #('pt', gettext('Portugues')),
)

DEFAULT_LANGUAGE = 0

#FIXTURE_DIRS = ['fixtures']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


LOCALE_PATHS = ('locale', )

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr-CA'

TIME_ZONE = 'America/Montreal'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join('staticfiles')
#STATIC_ROOT = '/home/ottawad6/staticfiles_django'
#STATIC_ROOT = '/home/ottawad6/www/django_staticfiles'
STATIC_ROOT = '/home4/ottawad6/django_projects/uopy/django_staticfiles'
#List of directories that Django could find my Static files
STATICFILES_DIRS = (
    os.path.join('static'),
    #os.path.join(BASE_DIR, 'applications/events/templates/events/static/events'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


from django.core.urlresolvers import reverse_lazy

#Sets the login logout URL
#LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
#LOGIN_URL = reverse_lazy('login')
#LOGOUT_URL = reverse_lazy('logout')

#django-registration-redux
ACCOUNT_ACTIVATION_DAYS = 1

# python-social-auth settings
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    #'account.authentication.EmailAuthBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-78677262-1'
