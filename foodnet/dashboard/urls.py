# -*- coding: utf-8 -*-

from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'foodnet.dashboard.views.home', name='home'),
]
