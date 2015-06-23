"""
Dashboard urlconf, included by foodnet.urls

Final namespace of these URLs:

foodnet:dashboard:url_name
"""

from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'foodnet.dashboard.views.home', name='home'),
]
