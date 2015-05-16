import logging

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from allauth.account.models import EmailAddress
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_username, user_email, user_field

from foodnet.membership.models import Invitation


log = logging.getLogger(__name__)


class FoodnetAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_redirect_url(self, request):
        log.debug("get_email_confirmation_redirect_url")
        return reverse('home')

    def is_open_for_signup(self, request):
        """
        You can override this method to, for example, inspect the session
        to check if an invitation was accepted.
        """
        log.debug("is_open_for_signup")
        return settings.SITE_OPEN_FOR_SIGNUP

    #def stash_verified_email(self, request, email):
    #    pass#
#
#    def unstash_verified_email(self, request):
#        pass

    def is_email_verified(self, request, email):
        """
        Checks whether or not the email address is already verified
        beyond allauth scope, for example, by having accepted an
        invitation before signing up.
        """
        log.debug("is_email_verified")
        ret = Invitation.objects.filter(email__iexact=email,
                                        accepted=True).count()
        return bool(ret)

    def clean_email(self, email):
        """
        Validates an email value. You can hook into this if you want to
        (dynamically) restrict what email addresses can be chosen.
        """
        log.debug("clean_email")
        email = forms.fields.EmailField().clean(value=email)
        is_taken = EmailAddress.objects\
            .filter(email__iexact=email).count() or \
            get_user_model().objects.filter(email__iexact=email).count()
        if is_taken:
            raise forms.ValidationError(_("This email is already taken. "
                                          "Please choose another."))
        return email
