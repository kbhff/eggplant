from django.shortcuts import render
from eggplant.market.models import Product


def role(request, role):
    if role == 'purchaser':
        return purchaser(request)
    elif role == 'communicator':
        return communicator(request)
    elif role == 'packer':
        return packer(request)
    elif role == 'cashier':
        return cashier(request)
    elif role == 'accountant':
        return accountant(request)


def purchaser(request):
    show_disabled_products = 'show-disabled-products' in request.GET
    if show_disabled_products:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(enabled=True)
    ctx = {
        'products': products,
        'show_disabled_products': show_disabled_products
    }
    return render(request, 'eggplant/roles/purchaser/dashboard.html', ctx)


def communicator(request):
    return render(request, 'eggplant/roles/communicator/dashboard.html')


def packer(request):
    return render(request, 'eggplant/roles/packer/dashboard.html')


def cashier(request):
    return render(request, 'eggplant/roles/cashier/dashboard.html')


def accountant(request):
    return render(request, 'eggplant/roles/accountant/dashboard.html')
