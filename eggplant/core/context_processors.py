
from django.conf import settings
from django.core.urlresolvers import reverse


def coop_vars(request):
    return {
        'COOP_NAME': settings.COOP_NAME,
        'COOP_DESCRIPTION': settings.COOP_DESCRIPTION,
        'COOP_LOGO': settings.COOP_LOGO,
        'SIGNUP_URL': reverse(settings.SIGNUP_URL_NAME),
    }
