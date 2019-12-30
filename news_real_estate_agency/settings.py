# -*- coding: utf-8 -*-
"""
Django settings for news_real_estate_agency project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')i$u(pp5v=1aaw0setg+q7w@q*6hng%-&bse@+a+zsps4*sn7j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'realty',
    'django_cleanup',
    'crispy_forms',
    'account',



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

ROOT_URLCONF = 'news_real_estate_agency.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),

                os.path.join(BASE_DIR, 'realty/templates'),
                os.path.join(BASE_DIR, 'contact/templates'),
                os.path.join(BASE_DIR, 'account/templates'),



                 ]
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

WSGI_APPLICATION = 'news_real_estate_agency.wsgi.application'





# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_style_css"),#подклуюить css
)



#для загруски файлов
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



#
#CKEDITOR-----------------------
#https://github.com/django-ckeditor/django-ckeditor
# http://django-wysiwyg.readthedocs.org/en/latest/examples.html

#https://github.com/django-ckeditor/django-ckeditor#installation


#DJANGO_WYSIWYG_FLAVOR = 'ckeditor' # редактор по умолчанию
#DJANGO_WYSIWYG_MEDIA_URL = STATIC_URL + "ckeditor/" # следить, если глюканет, отключить



# https://github.com/shaunsephton/django-ckeditor#using-s3





CKEDITOR_CONFIGS = { # все инструметы редактированья текста
    'default': {
        'toolbar': 'full',
         'height': 300,
         'width': 800,

    },
}


CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_RESTRICT_BY_USER = True # пользователь видит только свои файлы
#CKEDITOR------------------------


#django-geoposition------------------------------
#https://github.com/philippbosch/django-geoposition

GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCnZDIWTUThaxMRSsy6BazNadEXdvL69fo'

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 15,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}

#django-geoposition------------------------------

GOOGLE_MAPS_API_KEY = 'AIzaSyCnZDIWTUThaxMRSsy6BazNadEXdvL69fo'


#Настрака формы обратная связи
from emailsettings import *

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True



#django-crispy-forms.
CRISPY_TEMPLATE_PACK = 'bootstrap3'


"LOGIN_URL: URL для перенаправления пользователя на вход (например, представления с помощью декоратора login_required )"

LOGIN_URL = 'login'

#переход авторизацыи пользователя на главную стараницу
LOGIN_REDIRECT_URL =  '/realty/'





