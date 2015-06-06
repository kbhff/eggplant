# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

import logging


log = logging.getLogger(__file__)


def home(request):
    """home page"""
    ctx = {
           'title': 'dashboard'
    }
    return render(request, 'foodnet/dashboard/home.html', ctx)
