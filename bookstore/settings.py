"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from environs import Env


# Environment variables
env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG")

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # must add when adding SITE_ID

    # 3rd party
    'crispy_forms',
    'allauth',
    'allauth.account',

    # local
    'accounts',
    'pages',
    'books',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'bookstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="postgres://postgres@db/postgres")
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)  # location of static files in local development
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))  # location of static files in production
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',  # looks within STATICFILES_DIRS
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',  # looks across entire project for any directory named 'static'
]  # tells Django how to look for static files

# Media
MEDIA_URL = '/media/'  # absolute file system path
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))  # URL for templates

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
AUTH_USER_MODEL = 'accounts.CustomUser'

# django-allauth config
SITE_ID = 1
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default backend
    'allauth.account.auth_backends.AuthenticationBackend',  # allauth backend
)
ACCOUNT_SESSION_REMEMBER = True  # remove "Remember Me" box in login
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False  # removes the need to enter password twice in signup
ACCOUNT_USERNAME_REQUIRED = False  # sets username not required for user
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # sets email for login
ACCOUNT_EMAIL_REQUIRED = True  # sets email as an required field
ACCOUNT_UNIQUE_EMAIL = True  # sets email as a unique field

# E-mail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # output emails to the console
DEFAULT_FROM_EMAIL = 'admin@bookstore.com'  # default email origin
