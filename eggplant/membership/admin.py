from django.contrib import admin


from .models import UserProfile, Department, DepartmentInvitation, Account,\
    AccountCategory, AccountMembership


admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(DepartmentInvitation)
admin.site.register(Account)
admin.site.register(AccountCategory)
admin.site.register(AccountMembership)
