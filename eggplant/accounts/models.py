from django.db import models


class Account(models.Model):
    category = models.ForeignKey(
        'accounts.AccountCategory',
        related_name='accounts',
    )
    department = models.ForeignKey(
        'departments.Department',
        related_name='accounts',
    )

    start = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(null=True, default=None, blank=True)

    active = models.BooleanField(default=True)

    profiles = models.ManyToManyField(
        'profiles.UserProfile',
        through='accounts.AccountMembership',
        related_name='accounts'
    )

    def __str__(self):
        is_active = 'active' if self.active else 'inactive'
        return "{} {} {}".format(self.category, self.department, is_active)


class AccountMembership(models.Model):
    ROLE_NORMAL = 'normal'
    ROLE_OWNER = 'owner'
    ROLES = [
        (ROLE_NORMAL, 'Normal'),
        (ROLE_OWNER, 'Owner'),
    ]

    user_profile = models.ForeignKey('profiles.UserProfile')
    account = models.ForeignKey('accounts.Account')
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
        return '{} <-> {}'.format(self.account.id,
                                  self.user_profile.user.email)


class AccountCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
