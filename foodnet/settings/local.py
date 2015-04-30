import sys
from foodnet.settings.base import *


INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

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
     '--cover-branches',
     '--with-coverage',
     '--cover-erase',
     '--cover-package=foodnet',
     'foodnet',
]

for arg in sys.argv:
    if arg.startswith('--tests='):
        NOSE_ARGS = [
            '--verbosity=2',
            '--stop',
            '--with-yanc',
        ]
        break
