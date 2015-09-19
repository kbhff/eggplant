
from django.conf.urls import url

from eggplant.payments import views

urlpatterns = [
    url(r'orders-list/$', views.orders_list, name="orders_list"),

    url(r'order-detail/(?P<pk>\d+)/$',
        views.order_detail,
        name="order_detail"),

    url(r'order-info/(?P<pk>\d+)/$',
        views.order_info,
        name="order_info"),

    url(r'payment-accepted/(?P<pk>\d+)/$',
        views.payment_accepted,
        name="payment_accepted"),

    url(r'payment-rejected/(?P<pk>\d+)/$',
        views.payment_rejected,
        name="payment_rejected"),
    url(r'$', views.payments_home, name="payments_home"),
]
