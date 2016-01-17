# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0003_roleassignment_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roleassignment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user', related_name='roles'),
        ),
    ]
