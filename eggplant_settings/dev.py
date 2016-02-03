"""
Default settings for development
"""
from .base import *  # @UnusedWildImport
import sys

DEBUG = True

SECRET_KEY = 'BLAH BLAH BLAH'

# Show all console output
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['loggers']['eggplant']['level'] = 'DEBUG'

# Use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.sqlite',
    }
}

SITE_ID = 1
DOMAIN = 'localhost'
DEFAULT_HTTP_PROTOCOL = 'http'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'dev@eggplant.dk'
SERVER_EMAIL = 'django@localhost'

ADMINS = ()


os.environ['RECAPTCHA_TESTING'] = 'True'

INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

# The Django Debug Toolbar will only be shown to these client IPs.
INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.33.1',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'HIDE_DJANGO_SQL': False,
}


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--verbosity=2',
    '--stop',
    '--with-yanc',
    # '--cover-branches',
    # '--with-coverage',
    # '--cover-erase',
    # '--cover-package=eggplant',
    'eggplant',
]

for arg in sys.argv:
    if arg.startswith('--tests='):
        NOSE_ARGS = [
            '--verbosity=2',
            '--stop',
            '--with-yanc',
        ]
        break
