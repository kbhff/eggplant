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
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shortname', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('allow_webmembers', models.BooleanField(default=True)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField(null=True, default=None)),
                ('active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(to='membership.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_dt', models.DateTimeField(null=True)),
                ('verification_key', models.UUIDField(unique=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(to='membership.Department')),
                ('invited_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_invite', 'Can send invitation'),),
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MemberCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('middle_name', models.CharField(max_length=30, null=True)),
                ('address', models.TextField(max_length=255)),
                ('postcode', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('tel2', models.CharField(max_length=15, null=True)),
                ('sex', models.CharField(max_length=1, choices=[('f', 'female'), ('m', 'male')])),
                ('date_of_birth', models.DateField(null=True)),
                ('privacy', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(null=True, to='membership.Member')),
                ('user', models.OneToOneField(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='category',
            field=models.ForeignKey(to='membership.MemberCategory'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='member_category',
            field=models.ForeignKey(to='membership.MemberCategory'),
        ),
        migrations.AddField(
            model_name='departmentmembership',
            name='member',
            field=models.ForeignKey(to='membership.Member'),
        ),
        migrations.AddField(
            model_name='department',
            name='category',
            field=models.ForeignKey(to='membership.DepartmentCategory'),
        ),
        migrations.AddField(
            model_name='department',
            name='members',
            field=models.ManyToManyField(through='membership.DepartmentMembership', to='membership.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='departmentmembership',
            unique_together=set([('member', 'department')]),
        ),
    ]
