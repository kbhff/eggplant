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
            name='Payment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('amount', models.DecimalField(max_digits=12, verbose_name='amount to be paid', decimal_places=2)),
                ('currency', models.CharField(default='DKK', choices=[('DKK', 'DKK'), ('PLN', 'PLN'), ('GBP', 'GBP')], max_length=3)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
