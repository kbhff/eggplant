
import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..models.inventory import Product
from ..models.cart import Basket


log = logging.getLogger(__name__)


@login_required
def market_home(request):
    products = Product.objects.filter(stock__gt=0, enabled=True)
    basket = Basket.objects.open_for_user(request.user)
    all_items = basket.items.all()
    ctx = {
        'basket': basket,
        'basket_items': all_items,
        'products': products
    }
    return render(request, 'eggplant/market/market_home.html', ctx)
