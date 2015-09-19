from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import getpaid


class Payment(models.Model):
    amount = models.DecimalField(
        _("amount to be paid"),
        decimal_places=2,
        max_digits=12,
    )
    account = models.ForeignKey('membership.Account')
    currency = models.CharField(max_length=3, default='DKK',
                                choices=settings.CURRENCIES)
    created = models.DateTimeField(auto_now_add=True, null=False,
                                   db_index=True)

    def get_absolute_url(self):
        return reverse('eggplant:webshop:order_info', kwargs={'pk': self.pk})

    def get_last_payment_status(self):
        payments = self.payments.all().order_by('-created_on')[:1]
        if payments:
            return payments[0].status

    def __str__(self):
        return "Payment#{} of {} {} ({})".format(
            self.id,
            self.amount,
            self.currency,
            self.get_last_payment_status(),
        )

    def is_ready_for_payment(self):
        return bool(self.total)

    class Meta:
        app_label = 'webshop'


GetPaidPayment = getpaid.register_to_payment(
    Payment,
    unique=False,
    related_name='payments'
)
