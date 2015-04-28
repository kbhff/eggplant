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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('shortname', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('webmembers', models.BooleanField()),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DivisionMembers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('division', models.ForeignKey(to='membership.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('middlename', models.CharField(max_length=255)),
                ('adr1', models.CharField(max_length=255)),
                ('adr2', models.CharField(max_length=255)),
                ('streetno', models.CharField(max_length=255)),
                ('floor', models.CharField(max_length=255)),
                ('door', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
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
            model_name='divisionmembers',
            name='member',
            field=models.ForeignKey(to='membership.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='divisionmembers',
            unique_together=set([('member', 'division')]),
        ),
    ]
