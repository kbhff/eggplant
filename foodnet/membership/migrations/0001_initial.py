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
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('division', models.ForeignKey(to='membership.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_dt', models.DateTimeField(null=True)),
                ('verification_key', models.UUIDField(default=uuid.uuid4, unique=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('division', models.ForeignKey(to='membership.Division')),
                ('invited_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_invite', 'Can send invitation'),),
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('number', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MemberCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('middle_name', models.CharField(max_length=30, null=True)),
                ('address', models.TextField(max_length=255)),
                ('postcode', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('tel2', models.CharField(max_length=15, null=True)),
                ('sex', models.CharField(max_length=1, choices=[('f', 'female'), ('m', 'male')])),
                ('dob', models.DateField(null=True)),
                ('privacy', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='category',
            field=models.ForeignKey(to='membership.MemberCategory'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation',
            name='member_category',
            field=models.ForeignKey(to='membership.MemberCategory'),
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
