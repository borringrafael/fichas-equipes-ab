from .settings import *
from .local_settings import *


DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['core']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Maceio'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
