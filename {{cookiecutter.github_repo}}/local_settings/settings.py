## These settings will overrid any default settings set in the standard Django app and the `hacko_settings.py` included in docker container

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG').lower() == "true")

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
    '{{cookiecutter.python_package_namespace}}.{{cookiecutter.python_subpackage}}'
]

DATABASE_ROUTERS = ['backend.router.ModelDatabaseRouter',]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'NAME': os.environ.get('POSTGRES_NAME'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'HOST': os.environ.get('POSTGRES_HOST'),
#         'PORT': os.environ.get('POSTGRES_PORT')
#     }
# }

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/{{cookiecutter.python_package_namespace}}/static/'
