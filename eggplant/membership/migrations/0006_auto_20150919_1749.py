# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_remove_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('', '-----'), ('f', 'female'), ('m', 'male')], max_length=1, default=''),
        ),
    ]
