from django.conf import settings
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered


from .models.inventory import Product, ProductCategory, ProductTax
from .models.cart import Basket
from .models import Payment, GetPaidPayment

from getpaid.admin import PaymentAdmin


try:
    admin.site.register(GetPaidPayment, PaymentAdmin)
except AlreadyRegistered:
    pass
admin.site.register(Payment)


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductTax)


if settings.DEBUG:
    admin.site.register(Basket)
