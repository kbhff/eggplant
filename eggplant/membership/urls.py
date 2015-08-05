"""
Membership urlconf, included by foodnet.urls

Final namespace of these URLs:

eggplant:membership:url_name
"""

from django.conf.urls import url

from ..membership import views

urlpatterns = [
    url(r'invite/$', views.invite, name="invite"),
    url(r'profile/$', views.profile, name="profile"),

    # These views are not related to allauth
    url(r'accept-invitation/(?P<verification_key>[a-z0-9]{32})$',
        views.accept_invitation,
        name="accept_invitation"),
    url(r'^accounts/password/set/$',
        views.sets_new_user_password,
        name='new_member_set_password'),

]
