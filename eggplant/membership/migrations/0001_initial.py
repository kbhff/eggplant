# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('number', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AccountMembership',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('role', models.CharField(choices=[('normal', 'Normal'), ('owner', 'Owner')], default='normal', max_length=10)),
                ('account', models.ForeignKey(to='membership.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('shortname', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('allow_webmembers', models.BooleanField(default=True)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentInvitation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
            name='DepartmentMembership',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField(null=True, default=None)),
                ('active', models.BooleanField(default=True)),
                ('account', models.ForeignKey(to='membership.Account')),
                ('department', models.ForeignKey(to='membership.Department')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('middle_name', models.CharField(null=True, max_length=30)),
                ('address', models.TextField(max_length=255)),
                ('postcode', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('tel2', models.CharField(null=True, max_length=15)),
                ('sex', models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=1)),
                ('date_of_birth', models.DateField(null=True)),
                ('privacy', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('account', models.ManyToManyField(through='membership.AccountMembership', to='membership.Account')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='accountmembership',
            name='user_profile',
            field=models.ForeignKey(to='membership.UserProfile'),
        ),
        migrations.AddField(
            model_name='account',
            name='category',
            field=models.ForeignKey(to='membership.AccountCategory'),
        ),
        migrations.AddField(
            model_name='account',
            name='department',
            field=models.ForeignKey(to='membership.Department'),
        ),
        migrations.AlterUniqueTogether(
            name='departmentmembership',
            unique_together=set([('account', 'department')]),
        ),
    ]
