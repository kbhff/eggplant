from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfilePermission(models.Model):
    """
    Link between a user profile and a permission.


    Example 1:
    Check if a user has user creation access to a department:

    can_add_users = department.userprofilepermission_set.filter(
        user_profile__user=request.user,
        permission__can_add_users=True
    ).exists()

    if can_add_users:
        print(obama_speech)


    Example 2:
    Check if user can manage an account:

    can_manage_account = account.userprofilepermission_set.filter(
        user_profile__user=request.user,
        permission__can_change_accounts=True,
    )

    if not can_manage_account:
        return HttpNotAllowed("piss off")


    TODO: Create decorators to manage this easier!

    """
    user_profile = models.ForeignKey('membership.UserProfile')
    permission = models.ForeignKey('membership.Permission')

    is_global = models.BooleanField(
        _("global"),
        help_text=_("This permission gives access across all departments"),
        default=False
    )

    department = models.ForeignKey(
        'membership.Department'
    )
    account = models.ForeignKey(
        'membership.Account'
    )


class Permission(models.Model):
    """
    Permission roles are a set of permissions. Permissions are modeled as
    booleans in this model.

    What can a user do? Examples from discussion of different roles:

    A user is a superuser: THIS IS FOR THE global User.is_superuser field!!

    A user can create and manage all departments. E.g. someone from the central
    commission can add a new department and close an existing one.

    A user is a department manager: Can create and delete accounts and user
    profiles for everyone in a department.

    A user is an "intro vagt", someone who can create new accounts

    A user is a team link: Can manage volunteer shifts

    + something about economy


    CONCEPT OF THIS MODEL: Create boolean fields for different permissions,
    create lots of them! We want to be very explicit.
    """

    name = models.CharField(
        verbose_name=_("name"),
        max_length=64
    )

    # NEVER USE THIS IN A LOOKUP! USE EXPLICIT FIELDS
    all_permissions = models.BooleanField(
        _("all permissions"),
        default=False,
        help_text=_("Grant all permissions")
    )

    def save(self, *args, **kwargs):
        if self.all_permissions:
            pass
        return models.Model.save(self, *args, **kwargs)
