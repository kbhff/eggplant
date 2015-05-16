from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User, UserProfile, Division, DivisionMember,\
    Invitation, Member, MemberCategory


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Division)
admin.site.register(DivisionMember)
admin.site.register(Invitation)
admin.site.register(Member)
admin.site.register(MemberCategory)
