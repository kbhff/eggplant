from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin

from getpaid.admin import PaymentAdmin

from .models import Payment, GetPaidPayment
try:
    admin.site.register(GetPaidPayment, PaymentAdmin)
except AlreadyRegistered:
    pass
admin.site.register(Payment)
