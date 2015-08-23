from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import logging


log = logging.getLogger(__file__)


@login_required
def home(request):
    """home page"""
    ctx = {}
    return render(request, 'eggplant/dashboard/home.html', ctx)
