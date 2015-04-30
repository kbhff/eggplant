# -*- coding: utf-8 -*-
from django.shortcuts import render

import logging


log = logging.getLogger(__file__)


def profile(request):
    """profile page"""
    ctx = {
           'title': 'profile'
    }
    return render(request, 'membership/profile.html', ctx)
