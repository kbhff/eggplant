# -*- coding: utf-8 -*-
import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from foodnet.common.utils import absolute_url_reverse






