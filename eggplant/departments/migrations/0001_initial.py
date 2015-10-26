# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('allow_webmembers', models.BooleanField(default=True)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentAdministrator',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(to='departments.Department')),
                ('profile', models.ForeignKey(to='profiles.UserProfile', related_name='administrator_for')),
            ],
        ),
    ]
