# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_remove_account_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentAdministrator',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(to='membership.Department')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male')], blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='departmentadministrator',
            name='profile',
            field=models.ForeignKey(to='membership.UserProfile', related_name='administrator_for'),
        ),
    ]
