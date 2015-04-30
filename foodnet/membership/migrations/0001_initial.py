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
            name='Division',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('shortname', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('allow_webmembers', models.BooleanField()),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DivisionMember',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('division', models.ForeignKey(to='membership.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('number', models.PositiveSmallIntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('middlename', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=2000)),
                ('postcode', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('tel2', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=1)),
                ('birthday', models.DateField(null=True)),
                ('privacy', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='divisionmember',
            name='member',
            field=models.ForeignKey(to='membership.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='divisionmember',
            unique_together=set([('member', 'division')]),
        ),
    ]
