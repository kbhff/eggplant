# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('total', models.DecimalField(max_digits=8, decimal_places=2, default=0)),
                ('currency', models.CharField(choices=[('DKK', 'DKK'), ('PLN', 'PLN'), ('GBP', 'GBP')], default='DKK', max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
