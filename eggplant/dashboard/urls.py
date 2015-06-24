"""
Dashboard urlconf, included by foodnet.urls

Final namespace of these URLs:

eggplant:dashboard:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
