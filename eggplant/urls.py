# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^membership/', include('eggplant.membership.urls', namespace='membership')),
    url(r'^', include('eggplant.dashboard.urls', namespace='dashboard')),
]
