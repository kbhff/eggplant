# -*- coding: utf-8 -*-
from django.conf import settings

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

import eggplant.profiles.views
from eggplant.dashboard import views as dashboard_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # allauth signup is disabled - we have our own signup flow
    url(r'^account/signup/$',
        RedirectView.as_view(url=settings.SIGNUP_URL_NAME, permanent=True),
        name='account_signup'),

    # override django-allauth password set and change views
    url(r'^account/password/set/$',
        eggplant.profiles.views.NewUserPassword.as_view(),
        name='account_set_password'),

    # override django-allauth logout so no confirmation is needed
    # see: http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Remove_the_logout-confirmation_step
    url(r'^account/logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'}),

    url(r'^getpaid/', include('getpaid.urls')),

    url(r'^account/', include('allauth.urls')),

    url(r'^', include('eggplant.urls', namespace='eggplant')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
