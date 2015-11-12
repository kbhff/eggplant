from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'signup/$', views.signup, name='signup'),
    url(r'$', views.Profile.as_view(), name='profile'),
]
