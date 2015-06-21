from django.contrib import admin


from .models import UserProfile, Department, DepartmentMembership,\
    DepartmentInvitation, Account, AccountCategory, AccountMembership


class DepartmentMembershipInline(admin.TabularInline):
    model = DepartmentMembership
    extra = 1


admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(DepartmentMembership)
admin.site.register(DepartmentInvitation)
admin.site.register(Account)
admin.site.register(AccountCategory)
admin.site.register(AccountMembership)
