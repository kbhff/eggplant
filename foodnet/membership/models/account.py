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
    category = models.ForeignKey(
        'membership.AccountCategory',
        related_name='accounts',
    )
    department = models.ForeignKey(
        'membership.Department',
        related_name='accounts',
    )

    start = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(null=True, default=None)

    active = models.BooleanField(default=True)

    profiles = models.ManyToManyField(
        'membership.UserProfile',
        through='membership.AccountMembership',
    )


class AccountCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
