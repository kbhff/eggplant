from django import forms
from allauth.account.forms import BaseSignupForm, SetPasswordForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import user_email, setup_user_email, \
    cleanup_email_addresses
from allauth.account.models import EmailAddress
from captcha.fields import ReCaptchaField

from .models import (
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
