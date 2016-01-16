from django.shortcuts import render

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
    return render(request, 'eggplant/roles/purchaser.html')


def communicator(request):
    return render(request, 'eggplant/roles/communicator.html')


def packer(request):
    return render(request, 'eggplant/roles/packer.html')


def cashier(request):
    return render(request, 'eggplant/roles/cashier.html')


def accountant(request):
    return render(request, 'eggplant/roles/accountant.html')
