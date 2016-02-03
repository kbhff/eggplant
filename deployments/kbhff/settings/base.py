from eggplant_settings.base import BASE_DIR
import os

COOP_NAME = 'Københavns Fødevarefællesskab'
COOP_DESCRIPTION = ('Økologiske fødevarer — '
                    'til fair priser — '
                    'gennem arbejdende fællesskab')

WSGI_APPLICATION = 'deployments.kbhff.wsgi.application'

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'), )
