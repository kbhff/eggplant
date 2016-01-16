
import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from ..models.inventory import Product, ProductCategory
from ..models.cart import Basket
from ..filters import ProductFilter
from ..forms import ProductForm

log = logging.getLogger(__name__)


@login_required
def market_home(request, category_id=None):
    default_filters = dict(stock__gt=0, enabled=True)
    queryset = Product.objects.filter(**default_filters)
    product_filter = ProductFilter(request.GET, queryset=queryset)
    categories = ProductCategory.objects.filter(enabled=True)
    basket = Basket.objects.open_for_user(request.user)
    all_items = basket.items.all()
    ctx = {
        'basket': basket,
        'basket_items': all_items,
        'product_filter': product_filter,
        'product_categories': categories,
    }
    return render(request, 'eggplant/market/market_home.html', ctx)


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.save()
        if form.is_valid():
            return HttpResponseRedirect('eggplant/market/market_home.html')
    else:
        ctx = {
            'form': ProductForm()
        }
        return render(request, 'eggplant/market/add_product.html', ctx)
