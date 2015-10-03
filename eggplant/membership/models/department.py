from django.db import models


class Department(models.Model):
    """
    This can be a local office of a regional food coop.

    A person/group is a member of a food coop. But their membership can be
    of a specific single department.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
