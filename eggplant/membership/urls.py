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

    url(r'^departments/(?P<department_name>[\w\d\-]{1,10})/profiles$',
        views.departments_profiles,
        name='department_profiles'),

    url(r'^admin_profile/(?P<user_id>[0-9]{1,100})$',
        views.admin_profile,
        name='admin_profile'),

]
