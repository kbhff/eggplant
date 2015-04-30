# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, url

from foodnet.membership import views


urlpatterns = [
    url(r'profile/$', views.profile, name="profile"),
]
