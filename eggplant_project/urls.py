# -*- coding: utf-8 -*-
from django.conf import settings

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import eggplant.profiles.views
from eggplant.dashboard import views as dashboard_views


eggplant_urls = [
    url(
        r'^invitations/',
        include(
            'eggplant.invitations.urls',
            namespace='invitations',
            app_name='invitations',
        )
    ),

    url(
        r'^profile/',
        include(
            'eggplant.profiles.urls',
            namespace='profiles',
            app_name='profiles',
        )
    ),

    url(
        r'^department/',
        include(
            'eggplant.departments.urls',
            namespace='departments',
            app_name='departments',
        )
    ),

    url(
        r'^accounts/',
        include(
            'eggplant.accounts.urls',
            namespace='accounts',
            app_name='accounts',
        )
    ),

    url(r'^market/', include('eggplant.market.urls',
                             namespace='market')),
    url(r'^', include('eggplant.dashboard.urls',
                      namespace='dashboard')),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # signup is disabled - we only allow invited users
    url(r'^account/signup/$', dashboard_views.home, name='account_signup'),

    # override django-allauth password set and change views
    url(r'^account/password/change/$',
        eggplant.profiles.views.PasswordChangeView.as_view(),
        name='account_change_password'),
    url(r'^account/password/set/$',
        eggplant.profiles.views.NewUserPassword.as_view(),
        name='account_set_password'),

    url(r'^getpaid/', include('getpaid.urls')),

    url(r'^account/', include('allauth.urls')),

    url(r'^', include(eggplant_urls, namespace='eggplant')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
