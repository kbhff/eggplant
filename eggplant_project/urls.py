# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'eggplant.dashboard.views.home', name='home'),
    url(r'^membership/', include('eggplant.membership.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
