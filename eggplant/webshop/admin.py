from django.conf import settings
from django.contrib import admin


from .models.inventory import Product, ProductCategory, ProductTax
from .models.cart import Basket


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductTax)


if settings.DEBUG:
    admin.site.register(Basket)
