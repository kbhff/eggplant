from django.db import models


class Department(models.Model):
    shortname = models.CharField(max_length=4)
    name = models.CharField(max_length=255)

    # old system: webmembers
    allow_webmembers = models.BooleanField(default=True)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DepartmentMembership(models.Model):
    account = models.ForeignKey('membership.Account')
    department = models.ForeignKey('membership.Department')
    start = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(null=True, default=None)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = (('account', 'department'),)
