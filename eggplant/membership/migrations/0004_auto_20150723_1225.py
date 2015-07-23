# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20150723_0925'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accountmembership',
            unique_together=set([('user_profile', 'account')]),
        ),
    ]
