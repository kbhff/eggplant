# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from eggplant.dashboard import views as dashboard_views
from eggplant.membership import views as membership_views


eggplant_urls = [

    url(r'^membership/', include('eggplant.membership.urls',
                                 namespace='membership')),
    url(r'^payments/', include('eggplant.payments.urls',
                               namespace='payments')),
    url(r'^', include('eggplant.dashboard.urls',
                      namespace='dashboard')),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # signup is disabled - we only allow invited users
    url(r'^account/signup/$', dashboard_views.home, name='account_signup'),

    # override django-allauth password set and change views
    url(r'^account/password/change/$',
        membership_views.loginpage_password_change,
        name='account_change_password'),

    url(r'^account/', include('allauth.urls')),
    url(r'^getpaid/', include('getpaid.urls')),

    url(r'^', include(eggplant_urls, namespace='eggplant')),
]
