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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('middle_name', models.CharField(null=True, max_length=30)),
                ('address', models.TextField(max_length=255)),
                ('postcode', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('tel2', models.CharField(null=True, max_length=15)),
                ('sex', models.CharField(blank=True, choices=[('female', 'female'), ('male', 'male'), ('other', 'other')], max_length=100)),
                ('date_of_birth', models.DateField(null=True)),
                ('privacy', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
    ]
