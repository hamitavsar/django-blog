"""
Django settings for firstLesson project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a_&t$$++h2yqjt6b&%j*&#7tf!m3-d=#zr5%ne2e)5a_*^a$h5'

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
    'article',
    'User',
    'crispy_forms',
    'ckeditor',
    'django_cleanup.apps.CleanupConfig',
    
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

ROOT_URLCONF = 'firstLesson.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #Also we must to add this code for file upload.
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'firstLesson.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'tr-tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
#css, js ve image gibi görsellerimizi aşşağıdaki yöntem ile
#ana klasörümüzde oluşturduğumuz "static" klasörünü kullanarak
# css ve js dosyalarını kullanabiliyoruz. 
STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, "static")
]

# Aşşağıdaki yöntem ile 'admin' paneli dahil bütün css, js ve img dosyalarını 
# Tek bir yerde toplar ve Django bu yöntemi sistem gerçek bir sunucuya aktarıldığında
# Sistemde sorun olmaması için bu yöntemi önermektedir.
# Bu işi yaptıkdan sonra " python manage.py collectstatic "
# komutunu kullanmamız gerekli
STATIC_ROOT=os.path.join(BASE_DIR, "staticfiles")

#CRISPY TEMPLATE PACK
CRISPY_TEMPLATE_PACK = 'boostrap4'


#CK Editörü kullanırken her hangi bir inputu kod ile tanımlamak  istersek örneğin source kısmına <h2> selam </h2> yazdığımızda view kısmında
#sadece selam yazısını görmemiz için aşşağıda ki kuralı ekliyoruz. Not: Installed_Apps kısmına CKEditoru tanımlamayı unutma

CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
    }
}

#We added their for upload image but we can use for different document upload.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')