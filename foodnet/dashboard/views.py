# -*- coding: utf-8 -*-
from django.shortcuts import render

import logging


log = logging.getLogger(__file__)


def home(request):
    """home page"""
    ctx = {}
    return render(request, 'foodnet/dashboard/home.html', ctx)
