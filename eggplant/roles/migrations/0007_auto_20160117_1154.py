# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0006_auto_20160117_1025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roleassignment',
            options={'ordering': ('role',)},
        ),
    ]
