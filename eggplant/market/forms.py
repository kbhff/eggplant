from django import forms
from django.forms import ModelForm
from djmoney.settings import CURRENCY_CHOICES

from .models.inventory import Product
from eggplant.core.widgets import MoneyWidget


class BasketItemForm(forms.Form):
    product = forms.ModelChoiceField(Product.objects.filter(stock__gt=0,
                                                            enabled=True))
    quantity = forms.fields.IntegerField(min_value=0, max_value=100,
                                         required=True)
    delivery_date = forms.fields.DateField(required=False)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'tax', 'stock']
        widgets = {'price': MoneyWidget()}
