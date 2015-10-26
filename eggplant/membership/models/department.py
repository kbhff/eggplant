from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    """
    This can be a local office of a regional food coop.

    A person/group is a member of a food coop. But their membership can be
    of a specific single department.
    """

    name = models.CharField(
        verbose_name=_("department name"),
        max_length=255,
        blank=False,
    )
    site = models.ForeignKey(
        'sites.Site',
        default=settings.SITE_ID
    )

    def __str__(self):
        return self.name
