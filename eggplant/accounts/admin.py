from django.contrib import admin

from . import models


class AccountMembershipInline(admin.TabularInline):
    model = models.AccountMembership


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    inlines = [AccountMembershipInline]


@admin.register(models.AccountCategory)
class AccountAdmin(admin.ModelAdmin):
    pass
