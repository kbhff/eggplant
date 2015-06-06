# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'foodnet.dashboard.views.home', name='home'),
    url(r'^membership/', include('foodnet.membership.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
