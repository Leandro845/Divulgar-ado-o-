from pathlib import Path
from django.contrib.messages import constants
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xitqf*-i)isx8f5n@mx78xl_$03=d$z+c#f8f)jrk!ll2hvtz6'

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
    'usuarios',    # Your custom app for user-related functionality
    'divulgar',    # Your custom app for pet listing
    'adotar',      # Your custom app for adoption requests
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'adote.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR, 'templates').joinpath()],  # Templates directory
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

# WSGI application
WSGI_APPLICATION = 'adote.wsgi.application'

# Database configuration (using environment variables)
DATABASES = {
    'default': {
        'ENGINE': os.environ['ENGINE'],      # Database engine (e.g., 'django.db.backends.postgresql')
        'NAME': os.environ['NAME'],          # Database name
        'USER': os.environ['USER'],          # Database username
        'PASSWORD': os.environ['PASSWORD'],  # Database password
        'HOST': os.environ['HOST'],          # Database host
        'PORT': os.environ['PORT'],          # Database port
    }
}

# Password validation settings
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    Path(BASE_DIR, 'templates/static').joinpath(),  # Directory for static files
]

# Media files (uploaded user content)
MEDIA_ROOT = Path(BASE_DIR, 'media').joinpath()
MEDIA_URL = 'media/'

# Default primary key field type for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Message tags configuration
MESSAGE_TAGS = {
    constants.DEBUG: 'alert-info',
    constants.INFO: 'alert-info',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success'
}

# Email backend (prints emails to console for debugging)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
