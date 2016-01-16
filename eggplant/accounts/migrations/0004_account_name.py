# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_user_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
