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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField(default=None, blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='department name')),
                ('site', models.ForeignKey(default=1, to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_at', models.DateTimeField(null=True)),
                ('verification_key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, help_text='Human readable name, not used for any lookups so can be anything', verbose_name='name')),
                ('all_permissions', models.BooleanField(default=False, help_text='Grant all permissions', verbose_name='all permissions')),
                ('can_add_user_profiles', models.BooleanField(default=False, help_text='Can add users to associated account or department, meaning that setting this value is only meaningful if an account or department is associated.', verbose_name='add users')),
                ('can_change_account', models.BooleanField(default=False, help_text="Can change associated accounts' data. If associated to a department, gives global access to change all the accounts. If associated to an account, only gives access to that account.", verbose_name='change account(s)')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=30, blank=True, help_text='Optional.', verbose_name='middle name')),
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
                ('permissions', models.ManyToManyField(blank=True, to='membership.Permission', verbose_name='permissions')),
                ('user', models.OneToOneField(related_name='profile', editable=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfilePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_global', models.BooleanField(default=False, help_text='This permission gives access across all departments', verbose_name='global')),
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
        migrations.AddField(
            model_name='account',
            name='user_profiles',
            field=models.ManyToManyField(to='membership.UserProfile'),
        ),
    ]
