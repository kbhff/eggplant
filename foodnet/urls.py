# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^membership/', include('foodnet.membership.urls', namespace='membership')),
    url(r'^', include('foodnet.dashboard.urls', namespace='dashboard')),
]
