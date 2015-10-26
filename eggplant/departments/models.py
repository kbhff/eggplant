from django.db import models
from django.utils.text import slugify


class Department(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    # old system: webmembers
    allow_webmembers = models.BooleanField(default=True)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(**kwargs)


class DepartmentAdministrator(models.Model):
    department = models.ForeignKey('departments.Department')
    profile = models.ForeignKey('profiles.UserProfile',
                                related_name='administrator_for')
    created = models.DateTimeField(auto_now_add=True)