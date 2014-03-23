"""
Django settings for pythonfinal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0!iflqq2qw5jz9zjrf3hz+5w08%h#1ipt+8dv5=ut%^%m9ao8t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    #'grappelli_extensions',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'esih_admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pythonfinal.urls'

WSGI_APPLICATION = 'pythonfinal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
     'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DataDjango',
        'USER': 'UserDjango',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
        }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
# Parse database configuration from $DATABASE_URL
import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
	"pythonfinal/static"
)


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

###########################################################################
#############       New Lines
###########################################################################

#MEDIA_ROOT = "pythonfinal\pythonfinal\static\Mes_Fichiers"

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'django.contrib.staticfiles.finders.FileSystemFinder',
# )

#TEMPLATE_CONTEXT_PROCESSORS = (
    #"django.core.context_processors.request",
#)

GRAPPELLI_ADMIN_TITLE = "Plateforme d'Administration de Gestion de Cours..."
#GRAPPELLI_EXTENSIONS_NAVBAR = 'extensions.Navbar'
#GRAPPELLI_EXTENSIONS_NAVBAR = 'grappelli_extensions.test_navbar.Navbar'
#GRAPPELLI_EXTENSIONS_SIDEBAR = 'grappelli_extensions.test_navbar.Sidebar'