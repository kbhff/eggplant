from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class RoleAssignment(models.Model):
    PURCHASER = 'purchaser'
    COMMUNICATOR = 'communicator'
    PACKER = 'packer'
    CASHIER = 'cashier'
    ACCOUNTANT = 'accountant'
    ROLE_CHOICES = (
        (PURCHASER, _('Purchaser')),
        (COMMUNICATOR,  _('Communicator')),
        (PACKER, _('Packer')),
        (CASHIER,  _('Cashier')),
        (ACCOUNTANT,  _('Accountant')),
    )

    role = models.CharField(
        max_length=100,
        choices=ROLE_CHOICES
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='roles',
        verbose_name=_("user")
    )
