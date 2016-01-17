# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0005_auto_20160116_2009'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='roleassignment',
            unique_together=set([('user', 'role')]),
        ),
    ]
