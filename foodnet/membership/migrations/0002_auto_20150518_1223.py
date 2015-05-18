# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitation',
            options={'permissions': (('can_invite', 'Can send invitation'),)},
        ),
    ]
