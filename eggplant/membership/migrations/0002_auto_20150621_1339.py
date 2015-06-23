# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='departmentmembership',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='departmentmembership',
            name='account',
        ),
        migrations.RemoveField(
            model_name='departmentmembership',
            name='department',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='account',
        ),
        migrations.AddField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='exit',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='profiles',
            field=models.ManyToManyField(to='membership.UserProfile', through='membership.AccountMembership'),
        ),
        migrations.AddField(
            model_name='account',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 13, 39, 1, 901643, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='category',
            field=models.ForeignKey(related_name='accounts', to='membership.AccountCategory'),
        ),
        migrations.AlterField(
            model_name='account',
            name='department',
            field=models.ForeignKey(related_name='accounts', to='membership.Department'),
        ),
        migrations.DeleteModel(
            name='DepartmentMembership',
        ),
    ]
