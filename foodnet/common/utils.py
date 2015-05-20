from django.conf import settings
from django.core.urlresolvers import reverse


def absolute_url_reverse(url_name=None, **kwargs):
    path = '/'
    if url_name:
        path = reverse(url_name, **kwargs)
    full_url = "{}://{}{}".format(settings.DEFAULT_HTTP_PROTOCOL,
                                  settings.DOMAIN, path)
    return full_url
