# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
        ('payments', '0002_add_default_fees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='account',
            field=models.ForeignKey(to='membership.Account', default=1),
            preserve_default=False,
        ),
    ]
