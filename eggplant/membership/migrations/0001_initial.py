# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField(null=True, default=None, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='department name', max_length=255)),
                ('site', models.ForeignKey(to='sites.Site', default=1)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentInvitation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_at', models.DateTimeField(null=True)),
                ('verification_key', models.UUIDField(editable=False, unique=True, default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('account_category', models.ForeignKey(to='membership.AccountCategory')),
                ('department', models.ForeignKey(to='membership.Department')),
                ('invited_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'permissions': (('can_invite', 'Can send invitation'),),
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='name', max_length=64)),
                ('all_permissions', models.BooleanField(help_text='Grant all permissions', verbose_name='all permissions', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=255)),
                ('postcode', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('tel2', models.CharField(max_length=15)),
                ('sex', models.PositiveSmallIntegerField(null=True, choices=[('', '-----'), (1, 'female'), (0, 'male'), (2, 'other')])),
                ('date_of_birth', models.DateField(null=True)),
                ('privacy', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(to='membership.Account', null=True, verbose_name='account')),
                ('permissions', models.ManyToManyField(to='membership.Permission', verbose_name='permissions', blank=True)),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL, editable=False, related_name='profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfilePermission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_global', models.BooleanField(help_text='This permission gives access across all departments', verbose_name='global', default=False)),
                ('department', models.ForeignKey(to='membership.Department')),
                ('permission', models.ForeignKey(to='membership.Permission')),
                ('user_profile', models.ForeignKey(to='membership.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='category',
            field=models.ForeignKey(related_name='accounts', to='membership.AccountCategory'),
        ),
        migrations.AddField(
            model_name='account',
            name='department',
            field=models.ForeignKey(related_name='accounts', to='membership.Department'),
        ),
    ]
