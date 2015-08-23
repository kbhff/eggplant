import logging
from uuid import uuid4

from django.contrib.auth.models import User
from allauth.account.models import EmailAddress, EmailConfirmation

from eggplant.membership.models import DepartmentInvitation


log = logging.getLogger(__name__)


def create_verified_user(invitation):
    password = uuid4().hex
    user = User.objects.create_user(invitation.email, invitation.email,
                                    password)
    req = None
    email_address = EmailAddress.objects\
        .add_email(req, user, invitation.email, confirm=False, signup=False)
    email_address.verified = True
    email_address.primary = True
    email_address.save()
    econfirm = EmailConfirmation(email_address=email_address,
                                 key=invitation.verification_key.hex)
    econfirm.save()
    return user


def is_active_account_owner(user):
    from .models import AccountMembership
    memberships = user.userprofile.accountmembership_set.all()
    if memberships.count() != 1:
        log.warn("User %s has no account or belong to more than one",
                 user.username)
        return False

    role = memberships[0].role
    account = memberships[0].account
    return role == AccountMembership.ROLE_OWNER and account.active
