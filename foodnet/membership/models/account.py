from django.db import models

class AccountMembership(models.Model):
    user_profile = models.ForeignKey('membership.UserProfile')
    account = models.ForeignKey('membership.Account')

    ROLE_NORMAL = 'normal'
    ROLE_OWNER = 'owner'
    ROLES = [
        (ROLE_NORMAL, 'Normal'),
        (ROLE_OWNER, 'Owner'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default=ROLE_NORMAL
    )


class Account(models.Model):
    number = models.PositiveSmallIntegerField()
    category = models.ForeignKey('membership.AccountCategory')
    department = models.ForeignKey('membership.Department')


class AccountCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{0}'.format(self.name)
