import os
from .base import *  # @UnusedWildImport


DEBUG = False

# This should be the deployment
ALLOWED_HOSTS = ['.example.com']


# Use the cached template loader so template is compiled once and read from
# memory instead of reading from disk on each load.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'foodnet'),
        'USER': os.getenv('DATABASE_USER', 'foodnet'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'foodnet123'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'oksz%^7x*o0$(bm8w%%6j0&$y+elk+w)x5%-7&gm3@r!xv-qoi'
)

# TODO: Move these settings to production?

SITE_ID = 1
DOMAIN = 'localhost'

# This is a setting used by allauth and foodnet
DEFAULT_HTTP_PROTOCOL = 'http'

EMAIL_HOST = os.getenv('EMAIL_HOST', '127.0.0.1')
EMAIL_PORT = os.getenv('EMAIL_PORT', 25)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = '[FoodNet]'
EMAIL_TIMEOUT = 5
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'Info <info@{0}>'.format(DOMAIN)
SERVER_EMAIL = 'Alerts <alerts@{0}>'.format(DOMAIN)

ADMINS = (
    ('Admin', 'admin@{0}'.format(DOMAIN)),
)
