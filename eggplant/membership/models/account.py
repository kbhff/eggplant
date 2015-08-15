import random

from django.db import models


class AccountMembership(models.Model):
    ROLE_NORMAL = 'normal'
    ROLE_OWNER = 'owner'
    ROLES = [
        (ROLE_NORMAL, 'Normal'),
        (ROLE_OWNER, 'Owner'),
    ]

    user_profile = models.ForeignKey('membership.UserProfile')
    account = models.ForeignKey('membership.Account')
    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default=ROLE_NORMAL
    )

    class Meta:
        unique_together = (
            ('user_profile', 'account'),
        )

    def __str__(self):
        return '{} <-> {}'.format(self.account.number,
                                  self.user_profile.user.email)


class Account(models.Model):
    number = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        'membership.AccountCategory',
        related_name='accounts',
    )
    department = models.ForeignKey(
        'membership.Department',
        related_name='accounts',
    )

    start = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(null=True, default=None, blank=True)

    active = models.BooleanField(default=True)

    profiles = models.ManyToManyField(
        'membership.UserProfile',
        through='membership.AccountMembership',
    )

    def __str__(self):
        is_active = 'active' if self.active else 'inactive'
        return "{} {}".format(self.number, is_active)


class AccountCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
