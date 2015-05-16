import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from allauth.account.models import EmailConfirmation

from foodnet.membership.models import UserProfile


log = logging.getLogger(__name__)


class InvitationBackend(ModelBackend):

    def authenticate(self, **credentials):
        User = get_user_model()
        email = credentials.get('email', credentials.get('username'))
        verification_key = credentials.get('password')

        if email:
            users = User.objects.filter(email__iexact=email,
                                        emailaddress__email__iexact=email,
                                        emailaddress__verified=True)
            confirmations = EmailConfirmation.objects.filter(
                key=verification_key, email_address__verified=True)
            if len(users) == 1 and len(confirmations) == 1:
                user = users[0]
                profile = UserProfile.get_for_user(user)
                if not profile.is_complete():
                    return user
                else:
                    log.debug("this is not a new user")
                    print(profile.__dict__)
            else:
                print(users)
                print(confirmations)
                log.debug("no or too many users or no or too many confirmations")
        else:
            log.debug("email not found")
