# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_roleassignment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='roleassignment',
            name='role',
            field=models.CharField(max_length=100, choices=[('purchaser', 'Purchaser'), ('communicator', 'Communicator'), ('packer', 'Packer'), ('cashier', 'Cashier'), ('accountant', 'Accountant')], default=None),
            preserve_default=False,
        ),
    ]
