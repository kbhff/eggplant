# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField(blank=True, null=True, default=None)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='department name')),
                ('site', models.ForeignKey(to='sites.Site', default=1)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_at', models.DateTimeField(null=True)),
                ('verification_key', models.UUIDField(unique=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('account_category', models.ForeignKey(to='membership.AccountCategory')),
                ('department', models.ForeignKey(to='membership.Department')),
                ('invited_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_invite', 'Can send invitation'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('all_permissions', models.BooleanField(verbose_name='all permissions', default=False, help_text='Grant all permissions')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('middle_name', models.CharField(blank=True, verbose_name='middle name', max_length=30, help_text='Optional.')),
                ('address', models.TextField(max_length=255)),
                ('postcode', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('tel2', models.CharField(max_length=15)),
                ('sex', models.PositiveSmallIntegerField(choices=[('', '-----'), (1, 'female'), (0, 'male'), (2, 'other')], null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('privacy', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(related_name='profiles', to='membership.Account', null=True, verbose_name='account')),
                ('permissions', models.ManyToManyField(to='membership.Permission', blank=True, verbose_name='permissions')),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL, editable=False, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfilePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('is_global', models.BooleanField(verbose_name='global', default=False, help_text='This permission gives access across all departments')),
                ('account', models.ForeignKey(to='membership.Account')),
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
