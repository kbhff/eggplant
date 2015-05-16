from django import forms
from .models import UserProfile
from django.core.mail import send_mail
from allauth.account.forms import BaseSignupForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import user_email, setup_user_email, \
    cleanup_email_addresses
from allauth.account.models import EmailAddress

from .models import MemberCategory, Division, UserProfile


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First name', required=True,
                                 max_length=30)
    middle_name = forms.CharField(label='Middle name', max_length=30,
                                  required=False)
    last_name = forms.CharField(label='Last name', required=True,
                                max_length=30)
    address = forms.CharField(widget=forms.Textarea, label='Address',
                              required=True, max_length=255)
    postcode = forms.CharField(label='Post code', required=True, max_length=30)
    sex = forms.ChoiceField(choices=UserProfile.SEX_CHOICES, required=True)
    dob = forms.DateField(label='Date of birth', required=True)
    privacy = forms.BooleanField(required=True)


class InviteForm(forms.Form):
    email = forms.fields.EmailField(required=True)
    member_category = forms\
        .ModelChoiceField(MemberCategory.objects.all(), required=True)
    division = forms.ModelChoiceField(Division.objects.all(), required=True)


class AcceptInvitationForm(forms.Form):
    email = forms.fields.EmailField(required=True)
    # FIXME: add captcha


class SignupForm(BaseSignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(SignupForm, self).clean()
        return self.cleaned_data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        self.signup(user)
        return user

    def signup(self, request, user):
        assert EmailAddress.objects.filter(user=user).count() == 0
        priority_addresses = []
        adapter = get_adapter()
        stashed_email = adapter.unstash_verified_email(request)
        if stashed_email:
            priority_addresses.append(EmailAddress(user=user,
                                                   email=stashed_email,
                                                   primary=True,
                                                   verified=True))
        email = user_email(user)
        if email:
            priority_addresses.append(EmailAddress(user=user,
                                                   email=email,
                                                   primary=True,
                                                   verified=False))
        addresses, primary = cleanup_email_addresses(request,
                                                     priority_addresses
                                                     + addresses)
        for a in addresses:
            a.user = user
            a.save()
        EmailAddress.objects.fill_cache_for_user(user, addresses)
        if (primary
                and email
                and email.lower() != primary.email.lower()):
            user_email(user, primary.email)
            user.save()
        return primary
