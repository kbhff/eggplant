from django import forms
from allauth.account.forms import BaseSignupForm, SetPasswordForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import user_email, setup_user_email, \
    cleanup_email_addresses
from allauth.account.models import EmailAddress
from captcha.fields import ReCaptchaField

from .models import (
    AccountCategory,
    Department,
    UserProfile,
    DepartmentInvitation,
)


class NewUserSetPasswordForm(SetPasswordForm):
    def save(self, *args, **kwargs):
        self.user.set_password(self.cleaned_data["password1"])
        self.user.save()


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First name', required=True,
                                 max_length=30)
    middle_name = forms.CharField(label='Middle name', max_length=30,
                                  required=False)
    last_name = forms.CharField(label='Last name', required=True,
                                max_length=30)
    address = forms.CharField(widget=forms.Textarea, label='Address',
                              required=True, max_length=255)
    city = forms.CharField(label='City', required=True, max_length=50)
    postcode = forms.CharField(label='Post code', required=True, max_length=30)
    tel = forms.CharField(label='Phone', required=True, max_length=15)
    sex = forms.ChoiceField(choices=UserProfile.SEX_CHOICES, required=False)
    date_of_birth = forms.DateField(label='Date of birth',
                                    required=False,
                                    widget=forms.DateInput(
                                        attrs={'id': 'dob_datepicker',
                                               'autocomplete': "off"}))
    privacy = forms.BooleanField(required=False)


class DepartmentInvitationForm(forms.ModelForm):
    email = forms.fields.EmailField(required=True)

    class Meta:
        model = DepartmentInvitation
        fields = ['department', 'account_category', 'email']


class AcceptInvitationForm(forms.Form):
    captcha = ReCaptchaField(attrs={'theme': 'clean'})


class SignupForm(BaseSignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

    def clean(self):
        return super().clean()

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
