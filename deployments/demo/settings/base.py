from eggplant_settings.base import BASE_DIR
import os

COOP_NAME = 'EggPlant Demo'
COOP_DESCRIPTION = 'How can people say they don´t eat eggplant?'

WSGI_APPLICATION = 'deployments.demo.wsgi.application'

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'), )
