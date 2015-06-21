# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeConfig',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('amount', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('application', models.CharField(max_length=1, choices=[('o', 'one off'), ('m', 'monthly'), ('q', 'quaterly'), ('a', 'annually')])),
                ('currency', models.CharField(max_length=3, default='DKK', choices=[('DKK', 'DKK'), ('PLN', 'PLN'), ('GBP', 'GBP')])),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('total', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('currency', models.CharField(max_length=3, default='DKK', choices=[('DKK', 'DKK'), ('PLN', 'PLN'), ('GBP', 'GBP')])),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
