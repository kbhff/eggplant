# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20150621_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='exit',
            field=models.DateTimeField(default=None, blank=True, null=True),
        ),
    ]
