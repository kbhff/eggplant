
from django.conf import settings


def coop_vars(request):
    return {
        'COOP_NAME': settings.COOP_NAME,
        'COOP_DESCRIPTION': settings.COOP_DESCRIPTION,
    }
