"""
Django settings for scootersite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ct%_(9#e1py*%*=*%ay5&th1b26#e&)$u27hhn-!vztd_4oj!%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'scootersite.urls'

TEMPLATE_DIRS = (os.path.join(PROJECT_DIR,'templates'),)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

WSGI_APPLICATION = 'scootersite.wsgi.application'


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static','scootersite')
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'cssProjects'),)
#STATICFILES_DIRS =  (os.path.join('scootersite', 'static'),

print('\nROOT:',STATIC_ROOT,'\nDIRS:',STATICFILES_DIRS,'\n')
                    
STATICFILES_FINDERS =('django.contrib.staticfiles.finders.FileSystemFinder',
                     'django.contrib.staticfiles.finders.AppDirectoriesFinder',)
STATICFILES_STORAGE = ('django.contrib.staticfiles.storage.StaticFilesStorage')


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
