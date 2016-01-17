from django.db import models
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField

from eggplant.core.utils import generate_upload_path


def do_upload_product_image(inst, filename):
    return generate_upload_path(inst, filename, dirname='product_images')


class Product(models.Model):
    title = models.CharField(
        _("title"),
        max_length=512
    )
    description = models.TextField(
        _("description"),
    )
    category = models.ForeignKey(
        'market.ProductCategory',
        verbose_name=_("category"),
    )
    price = MoneyField(
        _("price"),
        max_digits=12,
        decimal_places=2,
    )
    stock = models.PositiveIntegerField(
        _("stock"),
        blank=True,
        null=True,
        default=1,
        help_text=_("Items in stock, leave blank if endless quantity available.")
    )
    tax = models.ForeignKey('ProductTax', verbose_name=_("tax"))
    enabled = models.BooleanField(_("enabled"), default=True)
    image = models.ImageField(upload_to=do_upload_product_image, blank=True,
                              null=True)

    def __str__(self):
        return "{} {} ({})".format(self.id, self.title, self.category)

    class Meta:
        app_label = 'market'


class ProductCategory(models.Model):

    title = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(_("enabled"), default=True)

    class Meta:
        app_label = 'market'

    def __str__(self):
        return self.title


class ProductTax(models.Model):

    title = models.CharField(
        _("title"),
        max_length=512
    )
    description = models.TextField(
        _("description"),
    )
    enabled = models.BooleanField(_("enabled"), default=True)

    tax = models.DecimalField(
        _("tax"),
        help_text=_("A factor, e.g. '0.25' adds 25% to value in order."),
        max_digits=5,
        decimal_places=4
    )

    class Meta:
        app_label = 'market'

    def __str__(self):
        return "{} ({:f}%)".format(self.title, (self.tax * 100).normalize())
