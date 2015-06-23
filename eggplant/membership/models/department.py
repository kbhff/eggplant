from django.db import models


class Department(models.Model):
    shortname = models.CharField(max_length=4)
    name = models.CharField(max_length=255)

    # old system: webmembers
    allow_webmembers = models.BooleanField(default=True)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name
