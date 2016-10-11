
from django.conf import settings
from django.core.urlresolvers import reverse


def coop_vars(request):
    # This problem is solved in several CMS, like django-cms and Wagtail. But
    # since we don't rely on them, here's a quick naive implementation that
    # simply takes for granted that the first part of a URL is the language
    # code.. so that's like a contract. Any page we render, we assume to be
    # through i18n_patterns
    LANGUAGE_CHOOSER = {}
    for lang in settings.LANGUAGES:
        path_components = request.path.split("/")
        lang_path = ["", lang[0]] + path_components[2:]
        LANGUAGE_CHOOSER[lang[0]] = {
            'name': lang[1],
            'this_page': "/".join(lang_path),
            'selected': path_components[1] == lang[0],
        }
    return {
        'COOP_NAME': settings.COOP_NAME,
        'COOP_DESCRIPTION': settings.COOP_DESCRIPTION,
        'COOP_LOGO': settings.COOP_LOGO,
        'SIGNUP_URL': reverse(settings.SIGNUP_URL_NAME),
        'LANGUAGE_CHOOSER': LANGUAGE_CHOOSER,
    }
