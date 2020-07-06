
import os
#for set the size of upload impage
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160

#the municipality name
MUNICIPALITY_NAME='baladeya x'#used in email subject

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(2th@mrr4b*v^%c9&rs0*9jhltx%f22s8452k53leu(c0x4^ek'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True#set to False when hosting

ALLOWED_HOSTS = ['127.0.0.1',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',#app
    'captcha',#google recaptcha
    'import_export',#for import and export tabel model
    'baladeyaadmin',#app
    'crispy_forms',#styling the form
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

ROOT_URLCONF = 'baladeyaproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],#template directory 
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

WSGI_APPLICATION = 'baladeyaproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',#data base engine (sqlite,mysql,....)
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),#data base location
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'#languge code (english us)

TIME_ZONE = 'Etc/GMT-3'#make the time zone to lebanon

USE_I18N = True

USE_L10N = True

USE_TZ = True #Use time zone


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
#  ----------------------------------------------- STATIC AND MEDIA STUF
STATIC_URL = '/static/'#the url of the static file
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),#the static directory (os.path.join(BASE_DIR,'name of file on the behind of baladeyaproject'))
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')#media directory
MEDIA_URL = '/media/'#media url
# ----------------------------------------------- EMAIL STUF
EMAIL_HOST = 'smtp.gmail.com'#google servive
EMAIL_PORT = '587'#google gmail port
EMAIL_HOST_USER = 'ali.h.mousawi@gmail.com'#google account
EMAIL_HOST_PASSWORD = 'alimoussawi'#google account password
EMAIL_USE_TLS = True
# EMAIL_USE_SSL=False
#  ----------------------------------------------- Google recaptcha
RECAPTCHA_PRIVATE_KEY = '6LcuiPoUAAAAAFAoTOdCNbqZmRma0y0B8k1pqGrg'
RECAPTCHA_PUBLIC_KEY = '6LcuiPoUAAAAAM8dSiEz6Z27yUEoxMZcnzErtXaw'
 
LOGIN_URL='/adminbaladeya/login/'#when you not loginig in you directed to this page 
LOGIN_REDIRECT_URL ='/adminbaladeya/'#after login redirect to the specified view

CRISPY_TEMPLATE_PACK = 'bootstrap4'#crispy_form_style_view
