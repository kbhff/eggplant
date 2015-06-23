from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import UserProfile


class NewUserForceProfileMiddleware(object):
    def process_request(self, request):
        allowed_paths = (
            reverse('profile'),
            reverse('account_login'),
            reverse('account_logout'),
            reverse('new_member_set_password'),
        )
        if (
            request.user.is_authenticated() and
            not request.user.is_superuser and
            request.path not in allowed_paths
        ):
            profile = UserProfile.get_for_user(request.user)
            if not profile.is_complete():
                msg = "Please update your profile."
                messages.add_message(request, messages.WARNING, msg)
                return HttpResponseRedirect(reverse('profile'))
