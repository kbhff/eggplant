# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    
    # Membership URLs take precedence over allauth because they overwrite
    # some of them. Because of allauth's architecture, we cannot have a
    # namespace for this application
    url(r'^', include('foodnet.urls', namespace='foodnet')),
    url(r'^accounts/', include('foodnet.urls_allauth')),
]
