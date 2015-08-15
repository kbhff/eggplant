# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_auto_20150723_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
