from uuid import uuid4

from django.contrib.auth import get_user_model

from allauth.account.models import EmailAddress, EmailConfirmation


def create_verified_user(invitation):
    password = uuid4().hex
    User = get_user_model()
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
