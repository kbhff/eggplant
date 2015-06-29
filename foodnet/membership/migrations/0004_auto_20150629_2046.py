# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departmentadministrator',
            old_name='admin',
            new_name='profile'),
    ]
