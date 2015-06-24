"""
allauth urlconf where some of the views are replaced by foodnet.membership
views.

HAS TO BE INCLUDED SEPARATELY BECAUSE ALLAUTH DOESN'T SUPPORT BEING
IN OUR FOODNET URLCONF

Example:

    urlpatterns = [
        url(r'^', include('foodnet.urls', namespace='foodnet')),
        url(r'^accounts/', include('foodnet.urls_allauth')),
    ]

"""
from django.conf.urls import include, url
from foodnet.dashboard import views as dashboard_views
from foodnet.membership import views

urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),

    # signup is disabled - we only allow invited users
    url(r'^signup/$',
        dashboard_views.home,
        name='account_signup'),

    # override password set and change views
    url(r'^password/change/$',
        views.loginpage_password_change,
        name='account_change_password'),

    url(r'^', include('allauth.urls')),
]
