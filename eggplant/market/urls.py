
from django.conf.urls import url, include

from .views import cart
from .views import inventory
from .views import payment


uuid_re_param = '[a-zA-Z0-9]{8}\-?[a-zA-Z0-9]{4}\-?[a-zA-Z0-9]{4}\-?' + \
    '[a-zA-Z0-9]{4}\-?[a-zA-Z0-9]{12}'

payment_patterns = [
    url(r'payment-list/$', payment.payment_list, name="payment_list"),

    url(r'payment-detail/(?P<pk>\d+)/$',
        payment.payment_detail,
        name="payment_detail"),

    url(r'payment-info/(?P<pk>\d+)/$',
        payment.payment_info,
        name="order_info"),

    url(r'payment-accepted/(?P<pk>\d+)/$',
        payment.payment_accepted,
        name="payment_accepted"),

    url(r'payment-rejected/(?P<pk>\d+)/$',
        payment.payment_rejected,
        name="payment_rejected"),
    url(r'$', payment.payments_home, name="payments_home"),
]


urlpatterns = [
    url(r'payment/', include(payment_patterns)),
    url(r'add-to-cart/$', cart.add_to_cart, name="add_to_cart"),
    url(r'remove-from-cart/$', cart.remove_from_cart,
        name="remove_from_cart"),
    url(r'your-cart/$',
        cart.cart_details, name="cart_details"),
    url(r'checkout/$',
        cart.checkout, name="checkout"),
    url(r'$', inventory.webshop_home, name="webshop_home"),
]
