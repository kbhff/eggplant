import logging

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.account.adapter import DefaultAccountAdapter

from foodnet.membership.models import DepartmentInvitation


log = logging.getLogger(__name__)


class FoodnetAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_redirect_url(self, request):
        log.debug("get_email_confirmation_redirect_url")
        return reverse('foodnet:dashboard:home')

    def is_open_for_signup(self, request):
        return settings.SITE_OPEN_FOR_SIGNUP

    def is_email_verified(self, request, email):
        """
        Checks whether or not the email address is already verified
        beyond allauth scope, by having accepted an
        invitation before signing up.
        """
        ret = DepartmentInvitation.objects.filter(
            email__iexact=email,
            accepted=True
        ).count()
        return bool(ret)

    def clean_email(self, email):
        """
        Validates an email value. Dynamically restricts what email addresses
        can be chosen.
        """
        email = forms.fields.EmailField().clean(value=email)
        is_taken = (
            EmailAddress.objects.filter(email__iexact=email).exists() or
            User.objects.filter(email__iexact=email).exists()
        )
        if is_taken:
            raise forms.ValidationError(_("This email is already taken. "
                                          "Please choose another."))
        return email
