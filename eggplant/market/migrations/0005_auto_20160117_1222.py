# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20160117_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=1, null=True, blank=True, help_text='Items in stock, leave blank if endless quantity available.', verbose_name='stock'),
        ),
    ]
