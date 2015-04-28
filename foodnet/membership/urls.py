# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, url

all_urls = [
    'foodnet.membership.views',
    url(r'profile/$',
        'profile',
        name="profile"),
]

urlpatterns = patterns(*all_urls)