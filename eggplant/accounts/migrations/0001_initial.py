# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField(default=None, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AccountMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('role', models.CharField(default='normal', choices=[('normal', 'Normal'), ('owner', 'Owner')], max_length=10)),
                ('account', models.ForeignKey(to='accounts.Account')),
                ('user_profile', models.ForeignKey(to='profiles.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='category',
            field=models.ForeignKey(to='accounts.AccountCategory', related_name='accounts'),
        ),
        migrations.AddField(
            model_name='account',
            name='department',
            field=models.ForeignKey(to='departments.Department', related_name='accounts'),
        ),
        migrations.AddField(
            model_name='account',
            name='profiles',
            field=models.ManyToManyField(to='profiles.UserProfile', related_name='accounts', through='accounts.AccountMembership'),
        ),
        migrations.AlterUniqueTogether(
            name='accountmembership',
            unique_together=set([('user_profile', 'account')]),
        ),
    ]
