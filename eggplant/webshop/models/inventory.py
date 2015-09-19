from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    title = models.CharField(
        _("title"),
        max_length=512
    )
    description = models.TextField(
        _("description"),
    )
    category = models.ForeignKey(
        'webshop.ProductCategory',
        verbose_name=_("category"),
    )
    price = models.DecimalField(
        _("title"),
        help_text=_("Price of product without VAT and taxes."),
        default=0,
        max_digits=12,
        decimal_places=2
    )
    stock = models.PositiveIntegerField(
        _("stock"),
        null=True,
        default=1,
        help_text=_("Items in stock, leave blank if endless quantity available.")
    )
    tax = models.ForeignKey('ProductTax', verbose_name=_("tax"))
    enabled = models.BooleanField(_("enabled"), default=True)

    def __str__(self):
        return "{} {} ({})".format(self.id, self.title, self.category)


class ProductCategory(models.Model):

    title = models.CharField(max_length=70)
    description = models.TextField()
    enabled = models.BooleanField(_("enabled"), default=True)


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
