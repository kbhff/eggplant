from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


from . import models


class NewUserForceProfileMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated() and not request.user.is_superuser:
            allowed_paths = [reverse(urlname) for urlname in
                             settings.NEW_USER_FORCE_PROFILE_ALLOWED_URL_NAMES]
            if request.path not in allowed_paths:
                try:
                    profile = request.user.profile
                except models.UserProfile.DoesNotExist:
                    profile = None
                if not profile or not profile.is_complete():
                    msg = "Please update your profile."
                    messages.add_message(request, messages.WARNING, msg)
                    return HttpResponseRedirect(
                        reverse('eggplant:profiles:profile')
                    )
