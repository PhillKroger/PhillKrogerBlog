
from pathlib import Path
import os
import django_heroku
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-v@w!rmzn9g7m_-dbe2(h_(t*5_w8k!1k9gn=xqz#mc#2x98!28'
DEBUG = False

ALLOWED_HOSTS = ["https://phillkroger.herokuapp.com/",
                 "127.0.0.1",
                 "0.0.0.0",
                 "*",
                 "phillkroger.herokuapp.com"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phillkroger',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

ROOT_URLCONF = 'PhillKrogerBlogg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'PhillKrogerBlogg.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if 'DATABASE_URL' in os.environ:
    import dj_database_url

    DATABASES = {'default': dj_database_url.config()}


LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'formatters': {
    'verbose': {
        'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                   'pathname=%(pathname)s lineno=%(lineno)s '
                   'funcname=%(funcName)s %(message)s'),
        'datefmt': '%Y-%m-%d %H:%M:%S'
    },
    'simple': {
        'format': '%(levelname)s %(message)s'
    }
},
'handlers': {
    'null': {
        'level': 'DEBUG',
        'class': 'logging.NullHandler',
    },
    'console': {
        'level': 'INFO',
        'class': 'logging.StreamHandler',
        'formatter': 'verbose'
    }
},
'loggers': {
    'django': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'django.request': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': False,
    },
}}


django_heroku.settings(config=locals(), staticfiles=False,logging=False)