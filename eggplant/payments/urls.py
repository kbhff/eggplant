
from django.conf.urls import url

from eggplant.payments import views

urlpatterns = [
    url(r'payment-list/$', views.payment_list, name="payment_list"),

    url(r'payment-detail/(?P<pk>\d+)/$',
        views.payment_detail,
        name="payment_detail"),

    url(r'payment-info/(?P<pk>\d+)/$',
        views.payment_info,
        name="order_info"),

    url(r'payment-accepted/(?P<pk>\d+)/$',
        views.payment_accepted,
        name="payment_accepted"),

    url(r'payment-rejected/(?P<pk>\d+)/$',
        views.payment_rejected,
        name="payment_rejected"),
    url(r'$', views.payments_home, name="payments_home"),
]
