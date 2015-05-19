# -*- coding: utf-8 -*-
import logging

from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import FormView

from allauth.account.models import EmailConfirmation, EmailAddress
from allauth.account.views import sensitive_post_parameters_m,\
    PasswordSetView, PasswordChangeView

from foodnet.common.views import LoginRequiredMixinView
from .forms import ProfileForm, InviteForm, AcceptInvitationForm
from .models import Invitation, User, UserProfile
from .utils import create_verified_user


log = logging.getLogger(__name__)


@permission_required('membership.can_invite')
@login_required
def invite(request):
    """Invite a new email address."""
    form = InviteForm()
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            existing_user = User.objects.filter(email=email)
            existing_email = EmailAddress.objects.get_users_for(email=email)
            if existing_user or existing_email:
                msg = 'User {} already exists.'.format(email)
                messages.add_message(request, messages.ERROR, msg)
            else:
                Invitation.objects.create(
                    email=email,
                    invited_by=request.user,
                    division=form.cleaned_data['division'],
                    member_category=form.cleaned_data['member_category'])
                msg = 'Invitation has been send to {}'.format(email)
                messages.add_message(request, messages.SUCCESS, msg)
                return redirect(reverse('home'))
    ctx = {
        'form': form,
        'title': "send invitation",
    }
    return render(request, 'membership/invite.html', ctx)


def accept_invitation(request, verification_key):
    """Accept invitation."""
    if request.user.is_authenticated():
        msg = "You are already logged-in"
        messages.add_message(request, messages.WARNING, msg)
        return redirect(reverse('home'))
    invitation = get_object_or_404(Invitation,
                                   verification_key=verification_key,
                                   accepted=False)
    form = AcceptInvitationForm()
    if request.method == 'POST':
        form = AcceptInvitationForm(request.POST)
        if form.is_valid():
            email = invitation.email
            existing_user = User.objects.filter(email=email)
            existing_email = EmailAddress.objects.get_users_for(email=email)

            if existing_user or existing_email:
                msg = "You have already accepted invitation for this email."
                messages.add_message(request, messages.ERROR, msg)
                return redirect(reverse('home'))
            invitation.accepted = True
            invitation.save()
            create_verified_user(invitation)

            # authenticate user via InvitationBackend
            user = authenticate(username=invitation.email,
                                password=verification_key)
            if user:
                login(request, user)
                request.session['new-invited-user'] = True
                return redirect(reverse('new_member_set_password'))
            else:
                log.debug("user can not be authenticated")
        else:
            log.debug(form.errors)
            msg = 'Invalid captcha.'
            messages.add_message(request, messages.WARNING, msg)

    ctx = {
        'form': form,
        'verification_key': verification_key,
        'title': "accept invitation",
    }
    return render(request, 'membership/accept_invitation.html', ctx)


class NewUserPasswordView(LoginRequiredMixinView, PasswordSetView):
    """
    Set password only for a new user. Existing users can use password change.
    """
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        if not request.session.get('new-invited-user'):
            raise Http404()
        return super(NewUserPasswordView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        profile = UserProfile.get_for_user(self.request.user)
        if profile.is_complete() or \
                not request.session.pop('new-invited-user', False):
            # existing user
            raise Http404()
        return super(NewUserPasswordView, self).post(request, *args, **kwargs)

    @sensitive_post_parameters_m
    def dispatch(self, request, *args, **kwargs):
        """Overrides PasswordSetView.dispatch with the View.dispatch"""
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
sets_new_user_password = NewUserPasswordView.as_view()


class LoginAfterPasswordChangeView(LoginRequiredMixinView, PasswordChangeView):
    """
    After password change redirect to account_login.
    """
    success_url = reverse_lazy('account_login')
loginpage_password_change = LoginAfterPasswordChangeView.as_view()


class ProfileView(LoginRequiredMixinView, FormView):
    """Profile form view."""
    form_class = ProfileForm
    template_name = 'membership/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        self.objects = UserProfile.objects.get(user_id=self.request.user.id)
        return self.objects

    def get_initial(self):
        initial = {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
        }
        initial.update(self.get_object().__dict__)
        return initial

    def form_valid(self, form):
        user_id = self.request.user.id
        profile = UserProfile.get_for_user(self.request.user)
        if not profile.is_complete():
            msg = "Please update your profile."
            messages.add_message(self.request, messages.WARNING, msg)
        User.objects.filter(id=user_id)\
            .update(first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'])
        del form.cleaned_data['first_name']
        del form.cleaned_data['last_name']
        print(form.cleaned_data)
        UserProfile.objects.filter(user_id=user_id).update(**form.cleaned_data)
        msg = "Your profile has been successfully updated."
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super(ProfileView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['title'] = 'profile'
        context['form'] = kwargs['form']
        return context
profile = ProfileView.as_view()
