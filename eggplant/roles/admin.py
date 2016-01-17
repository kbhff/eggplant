from django.contrib import admin

from . import models


@admin.register(models.RoleAssignment)
class RoleAssignment(admin.ModelAdmin):
    pass
