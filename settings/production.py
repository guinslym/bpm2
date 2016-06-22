#import common configuration
from .base import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sldjf0h6urdfl%-bs=mc!%&ybj@=8a4rrqc^26t!6738*nf!l2ut8k#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['uopy.ca', 'www.uopy.ca',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'taggit',
    'applications.events',
)



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
            ],
        },
    },
]

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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
             'filename': BASE_DIR+'/logs/prod.log',
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
