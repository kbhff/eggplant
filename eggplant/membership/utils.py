import logging
from uuid import uuid4

from django.contrib.auth.models import User
from allauth.account.models import EmailAddress, EmailConfirmation


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


# TODO: This should be a property of the user and possibly a queryset method
# of the UserProfile manager.
def is_account_owner(user, account):
    return account.userprofilepermission_set.filter(
        user_profile__user=user,
        permission__can_change_accounts=True,
    ).exists()
